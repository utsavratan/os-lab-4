import unittest
from fs_lab.free_space import Bitmap, FreeList


class FreeSpaceTests(unittest.TestCase):
    def test_bitmap(self):
        bitmap = Bitmap(8)
        blocks = bitmap.allocate(3)
        self.assertEqual(blocks, [0, 1, 2])
        bitmap.release(blocks)
        self.assertEqual(bitmap.bits, [0] * 8)

    def test_free_list(self):
        fl = FreeList(8)
        blocks = fl.allocate(3)
        self.assertEqual(blocks, [0, 1, 2])
        fl.release(blocks)
        self.assertEqual(fl.free, list(range(8)))


if __name__ == "__main__":
    unittest.main()
