"""Contiguous, linked and indexed file-allocation simulations."""

from __future__ import annotations
from dataclasses import dataclass


class AllocationDisk:
    def __init__(self, blocks: int = 32):
        if blocks <= 0:
            raise ValueError("blocks must be positive")
        self.blocks = [None] * blocks

    def free_blocks(self) -> list[int]:
        return [i for i, owner in enumerate(self.blocks) if owner is None]

    def show(self):
        print("BLOCK MAP:")
        print(" ".join("." if owner is None else str(owner) for owner in self.blocks))


def contiguous_allocate(disk: AllocationDisk, filename: str, count: int) -> list[int]:
    if count <= 0:
        raise ValueError("count must be positive")
    print(f"\nCONTIGUOUS REQUEST: file={filename} blocks={count}")
    run = []
    for i, owner in enumerate(disk.blocks):
        if owner is None:
            run.append(i)
            if len(run) == count:
                break
        else:
            run = []
    if len(run) != count:
        raise MemoryError("no contiguous region available")
    for i in run:
        disk.blocks[i] = filename
    print(f"SELECTED CONTIGUOUS BLOCKS: {run}")
    disk.show()
    return run


def linked_allocate(disk: AllocationDisk, filename: str, count: int) -> list[int]:
    if count <= 0:
        raise ValueError("count must be positive")
    free = disk.free_blocks()
    if len(free) < count:
        raise MemoryError("insufficient free blocks")
    chosen = free[:count]
    for i in chosen:
        disk.blocks[i] = filename
    print(f"\nLINKED REQUEST: file={filename} blocks={count}")
    print(f"ALLOCATE: {chosen}")
    print("CHAIN:", " -> ".join(map(str, chosen)))
    disk.show()
    return chosen


def indexed_allocate(disk: AllocationDisk, filename: str, count: int) -> tuple[int, list[int]]:
    if count <= 0:
        raise ValueError("count must be positive")
    free = disk.free_blocks()
    if len(free) < count + 1:
        raise MemoryError("insufficient blocks for index + data")
    index_block = free[0]
    data = free[1:count + 1]
    disk.blocks[index_block] = f"{filename}:INDEX"
    for i in data:
        disk.blocks[i] = filename
    print(f"\nINDEXED REQUEST: file={filename} blocks={count}")
    print(f"INDEX BLOCK: {index_block}")
    print(f"DATA BLOCKS: {data}")
    print(f"INDEX TABLE: {dict(enumerate(data))}")
    disk.show()
    return index_block, data


def demo() -> None:
    print("\n=== FILE ALLOCATION METHODS ===")
    d1 = AllocationDisk(20)
    contiguous_allocate(d1, "A", 4)

    d2 = AllocationDisk(20)
    d2.blocks[2] = "X"
    d2.blocks[3] = "X"
    d2.blocks[9] = "Y"
    linked_allocate(d2, "B", 5)

    d3 = AllocationDisk(20)
    indexed_allocate(d3, "C", 4)
