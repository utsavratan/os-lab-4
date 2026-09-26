"""Integrated simulated filesystem independent of the host filesystem."""

from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class SimFile:
    name: str
    owner: str
    group: str
    permissions: str = "rw-r-----"
    data: str = ""
    blocks: list[int] = field(default_factory=list)
    allocation: str = "contiguous"


@dataclass
class SimDir:
    name: str
    parent: "SimDir | None" = None
    files: dict[str, SimFile] = field(default_factory=dict)
    dirs: dict[str, "SimDir"] = field(default_factory=dict)


class SimFS:
    def __init__(self, blocks: int = 32):
        if blocks <= 0:
            raise ValueError("blocks must be positive")
        self.root = SimDir("/")
        self.blocks = [None] * blocks

    def _allocate(self, filename: str, count: int, method: str) -> list[int]:
        free = [i for i, owner in enumerate(self.blocks) if owner is None]
        if len(free) < count:
            raise MemoryError("insufficient simulated disk space")

        if method == "contiguous":
            run = []
            for i in free:
                if not run or i == run[-1] + 1:
                    run.append(i)
                else:
                    run = [i]
                if len(run) == count:
                    chosen = run
                    break
            else:
                raise MemoryError("no contiguous space available")
        elif method == "linked":
            chosen = free[:count]
        elif method == "indexed":
            if len(free) < count + 1:
                raise MemoryError("insufficient space for index block")
            chosen = free[1:count + 1]
            self.blocks[free[0]] = f"{filename}:INDEX"
            print(f"  INDEX BLOCK: {free[0]}")
        else:
            raise ValueError("allocation must be contiguous, linked or indexed")

        for i in chosen:
            self.blocks[i] = filename
        print(f"  ALLOCATE {filename}: blocks={chosen} method={method}")
        return chosen

    def _free(self, file: SimFile) -> None:
        for block in file.blocks:
            if self.blocks[block] == file.name:
                self.blocks[block] = None
        # Release any index block associated with this filename.
        marker = f"{file.name}:INDEX"
        for i, owner in enumerate(self.blocks):
            if owner == marker:
                self.blocks[i] = None
                print(f"  RELEASE INDEX BLOCK: {i}")
        print(f"  RELEASE DATA BLOCKS: {file.blocks}")

    def create(self, name: str, owner: str = "utsav", group: str = "students",
               allocation: str = "contiguous", blocks: int = 1) -> SimFile:
        if "/" in name or not name:
            raise ValueError("file name must be a simple name")
        if name in self.root.files or name in self.root.dirs:
            raise FileExistsError(name)
        print(f"\nCREATE FILE: {name}")
        allocated = self._allocate(name, blocks, allocation)
        file = SimFile(name, owner, group, blocks=allocated, allocation=allocation)
        self.root.files[name] = file
        self.validate()
        return file

    def write(self, name: str, data: str, identity: str = "owner") -> None:
        file = self.root.files[name]
        if identity != "owner":
            raise PermissionError("simulated policy permits writes only by owner")
        print(f"\nWRITE FILE: {name} bytes={len(data.encode())}")
        file.data = data

    def read(self, name: str, identity: str = "owner") -> str:
        file = self.root.files[name]
        if identity not in {"owner", "group"}:
            raise PermissionError("read denied")
        print(f"\nREAD FILE: {name} -> {file.data!r}")
        return file.data

    def list(self) -> list[str]:
        entries = sorted(list(self.root.files) + list(self.root.dirs))
        print(f"\nLIST / -> {entries}")
        return entries

    def truncate(self, name: str, identity: str = "owner") -> None:
        file = self.root.files[name]
        if identity != "owner":
            raise PermissionError("truncate denied")
        print(f"\nTRUNCATE: {name}")
        self._free(file)
        file.blocks = []
        file.data = ""
        self.validate()

    def delete(self, name: str, identity: str = "owner") -> None:
        file = self.root.files[name]
        if identity != "owner":
            raise PermissionError("delete denied")
        print(f"\nDELETE FILE: {name}")
        self._free(file)
        del self.root.files[name]
        self.validate()

    def chmod(self, name: str, permissions: str, identity: str = "owner") -> None:
        if identity != "owner":
            raise PermissionError("chmod denied")
        if len(permissions) != 9:
            raise ValueError("permissions must contain 9 characters")
        file = self.root.files[name]
        print(f"\nCHMOD {name}: {file.permissions} -> {permissions}")
        file.permissions = permissions

    def validate(self) -> bool:
        expected_data = {}
        expected_index = set()

        for name, file in self.root.files.items():
            for block in file.blocks:
                if block < 0 or block >= len(self.blocks):
                    raise AssertionError(f"invalid block {block}")
                if block in expected_data:
                    raise AssertionError(f"block {block} allocated twice")
                expected_data[block] = name

            if file.allocation == "indexed":
                marker = f"{file.name}:INDEX"
                for index, owner in enumerate(self.blocks):
                    if owner == marker:
                        expected_index.add(index)
                        break
                else:
                    raise AssertionError(f"missing index block for {file.name}")

        for index, owner in enumerate(self.blocks):
            if index in expected_data:
                if owner != expected_data[index]:
                    raise AssertionError(f"block map mismatch for data block {index}")
            elif index in expected_index:
                continue
            elif owner is not None:
                raise AssertionError(f"orphan allocation at {index}")

        print("  CONSISTENCY CHECK: PASS")
        return True

    def block_map(self) -> list[str | None]:
        return self.blocks[:]


def demo() -> SimFS:
    print("\n=== INTEGRATED SIMULATED FILESYSTEM ===")
    fs = SimFS(24)
    fs.create("notes.txt", allocation="contiguous", blocks=3)
    fs.write("notes.txt", "Operating Systems practical")
    fs.read("notes.txt")
    fs.chmod("notes.txt", "rw-r-----")
    fs.create("linked.bin", allocation="linked", blocks=4)
    fs.create("indexed.dat", allocation="indexed", blocks=3)
    fs.list()
    fs.truncate("notes.txt")
    fs.delete("linked.bin")
    fs.list()
    fs.validate()
    return fs
