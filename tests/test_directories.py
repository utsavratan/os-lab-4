import unittest
from fs_lab.directories import single_level, two_level, tree_structure


class DirectoryTests(unittest.TestCase):
    def test_single(self):
        result = single_level(["a", "b"])
        self.assertEqual(sorted(result), ["a", "b"])

    def test_two_level(self):
        result = two_level({"u1": ["a"], "u2": ["a"]})
        self.assertEqual(list(result["u1"]), ["a"])
        self.assertEqual(list(result["u2"]), ["a"])

    def test_tree(self):
        result = tree_structure()
        self.assertIn("home", result)


if __name__ == "__main__":
    unittest.main()
