import unittest
from fs_lab.simulated_fs import SimFS


class SimFSTests(unittest.TestCase):
    def test_create_write_read(self):
        fs = SimFS(20)
        file = fs.create("a.txt", blocks=3)
        fs.write("a.txt", "hello")
        self.assertEqual(fs.read("a.txt"), "hello")
        self.assertEqual(len(file.blocks), 3)

    def test_delete_reclaims_blocks(self):
        fs = SimFS(10)
        fs.create("a", blocks=3)
        self.assertEqual(sum(x is None for x in fs.block_map()), 7)
        fs.delete("a")
        self.assertEqual(sum(x is None for x in fs.block_map()), 10)

    def test_truncate(self):
        fs = SimFS(10)
        fs.create("a", blocks=3)
        fs.write("a", "data")
        fs.truncate("a")
        self.assertEqual(fs.read("a"), "")
        self.assertEqual(fs.root.files["a"].blocks, [])

    def test_indexed(self):
        fs = SimFS(10)
        file = fs.create("indexed", allocation="indexed", blocks=2)
        self.assertEqual(len(file.blocks), 2)
        fs.validate()


if __name__ == "__main__":
    unittest.main()
