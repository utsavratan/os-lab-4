"""Safe real filesystem operations restricted to the project sandbox."""

from __future__ import annotations

import os
import shutil
import stat
from pathlib import Path


class SandboxFS:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def safe_path(self, relative: str | Path) -> Path:
        candidate = Path(relative)
        if candidate.is_absolute():
            raise ValueError("absolute paths are not allowed in the sandbox")
        if any(part == ".." for part in candidate.parts):
            raise ValueError("parent-directory traversal is not allowed")
        resolved = (self.root / candidate).resolve()
        if resolved != self.root and self.root not in resolved.parents:
            raise ValueError("path escapes the controlled sandbox")
        return resolved

    def mkdir(self, relative: str) -> Path:
        path = self.safe_path(relative)
        path.mkdir(parents=True, exist_ok=True)
        print(f"MKDIR   {path.relative_to(self.root)}")
        return path

    def write(self, relative: str, text: str) -> Path:
        path = self.safe_path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"WRITE   {path.relative_to(self.root)} bytes={len(text.encode())}")
        return path

    def append(self, relative: str, text: str) -> Path:
        path = self.safe_path(relative)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(text)
        print(f"APPEND  {path.relative_to(self.root)} bytes={len(text.encode())}")
        return path

    def read(self, relative: str) -> str:
        path = self.safe_path(relative)
        text = path.read_text(encoding="utf-8")
        print(f"READ    {path.relative_to(self.root)} bytes={len(text.encode())}")
        return text

    def copy(self, source: str, destination: str) -> Path:
        src = self.safe_path(source)
        dst = self.safe_path(destination)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"COPY    {src.relative_to(self.root)} -> {dst.relative_to(self.root)}")
        return dst

    def rename(self, source: str, destination: str) -> Path:
        src = self.safe_path(source)
        dst = self.safe_path(destination)
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)
        print(f"RENAME  {src.relative_to(self.root)} -> {dst.relative_to(self.root)}")
        return dst

    def delete(self, relative: str) -> None:
        path = self.safe_path(relative)
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
        print(f"DELETE  {Path(relative)}")

    def list_dir(self, relative: str = ".") -> list[str]:
        path = self.safe_path(relative)
        entries = sorted(p.name for p in path.iterdir())
        print(f"LIST    {Path(relative)} -> {entries}")
        return entries

    def metadata(self, relative: str) -> dict:
        path = self.safe_path(relative)
        st = path.stat()
        mode = stat.filemode(st.st_mode)
        info = {
            "path": str(path.relative_to(self.root)),
            "size": st.st_size,
            "mode": mode,
            "uid": st.st_uid,
            "gid": st.st_gid,
            "is_file": path.is_file(),
            "is_dir": path.is_dir(),
        }
        print(f"STAT    {info}")
        return info


def demo(root: Path) -> None:
    print("\n=== CONTROLLED REAL FILESYSTEM ===")
    fs = SandboxFS(root)

    demo_dir = fs.mkdir("demo")
    fs.write("demo/hello.txt", "Operating Systems\nFile-System Lab\n")
    print("CONTENT:", repr(fs.read("demo/hello.txt")))
    fs.append("demo/hello.txt", "Append operation verified.\n")
    print("CONTENT AFTER APPEND:", repr(fs.read("demo/hello.txt")))
    fs.copy("demo/hello.txt", "demo/copy.txt")
    fs.rename("demo/copy.txt", "demo/renamed.txt")
    fs.metadata("demo/renamed.txt")
    fs.list_dir("demo")
    fs.delete("demo/renamed.txt")
    fs.delete("demo/hello.txt")
    fs.delete("demo")
    print("RESULT: controlled sandbox demonstration completed safely.")
