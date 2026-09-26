import unittest
from fs_lab.access_methods import sequential_access, direct_access


class AccessTests(unittest.TestCase):
    def test_sequential(self):
        data = ["a", "b", "c"]
        self.assertEqual(sequential_access(data), data)

    def test_direct(self):
        data = ["a", "b", "c"]
        self.assertEqual(direct_access(data, [2, 0]), ["c", "a"])


if __name__ == "__main__":
    unittest.main()
