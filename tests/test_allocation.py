import unittest
from fs_lab.allocation import AllocationDisk, contiguous_allocate, linked_allocate, indexed_allocate


class AllocationTests(unittest.TestCase):
    def test_contiguous(self):
        disk = AllocationDisk(10)
        blocks = contiguous_allocate(disk, "A", 3)
        self.assertEqual(blocks, [0, 1, 2])

    def test_linked(self):
        disk = AllocationDisk(10)
        blocks = linked_allocate(disk, "B", 3)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(len(set(blocks)), 3)

    def test_indexed(self):
        disk = AllocationDisk(10)
        index, data = indexed_allocate(disk, "C", 3)
        self.assertNotIn(index, data)
        self.assertEqual(len(data), 3)


if __name__ == "__main__":
    unittest.main()
