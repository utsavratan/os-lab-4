"""Bitmap and free-list space-management simulations."""


class Bitmap:
    def __init__(self, blocks: int):
        if blocks <= 0:
            raise ValueError("blocks must be positive")
        self.bits = [0] * blocks

    def allocate(self, count: int) -> list[int]:
        if count <= 0:
            raise ValueError("count must be positive")
        free = [i for i, bit in enumerate(self.bits) if bit == 0]
        if len(free) < count:
            raise MemoryError("insufficient free blocks")
        selected = free[:count]
        for i in selected:
            self.bits[i] = 1
        print(f"\nBITMAP ALLOCATE {selected}")
        self.show()
        return selected

    def release(self, blocks: list[int]) -> None:
        for i in blocks:
            if i < 0 or i >= len(self.bits):
                raise IndexError(i)
            if self.bits[i] == 0:
                raise ValueError(f"block {i} is already free")
            self.bits[i] = 0
        print(f"\nBITMAP RELEASE {blocks}")
        self.show()

    def show(self):
        print("BITMAP:", "".join(map(str, self.bits)))


class FreeList:
    def __init__(self, blocks: int):
        if blocks <= 0:
            raise ValueError("blocks must be positive")
        self.free = list(range(blocks))

    def allocate(self, count: int) -> list[int]:
        if count <= 0:
            raise ValueError("count must be positive")
        if len(self.free) < count:
            raise MemoryError("insufficient free blocks")
        selected = self.free[:count]
        self.free = self.free[count:]
        print(f"\nFREE-LIST ALLOCATE {selected}")
        self.show()
        return selected

    def release(self, blocks: list[int]) -> None:
        for i in blocks:
            if i in self.free:
                raise ValueError(f"block {i} already free")
            self.free.append(i)
        self.free.sort()
        print(f"\nFREE-LIST RELEASE {blocks}")
        self.show()

    def show(self):
        print("FREE LIST:", self.free)


def demo() -> None:
    print("\n=== FREE-SPACE MANAGEMENT ===")
    bitmap = Bitmap(16)
    a = bitmap.allocate(4)
    b = bitmap.allocate(3)
    bitmap.release(a)
    bitmap.release(b)

    freelist = FreeList(16)
    c = freelist.allocate(5)
    freelist.release(c)
