import tempfile
import unittest
from pathlib import Path
from fs_lab.real_fs import SandboxFS


class RealFSTests(unittest.TestCase):
    def test_basic_operations(self):
        with tempfile.TemporaryDirectory() as tmp:
            fs = SandboxFS(Path(tmp))
            fs.mkdir("x")
            fs.write("x/a.txt", "hello")
            self.assertEqual(fs.read("x/a.txt"), "hello")
            fs.append("x/a.txt", " world")
            self.assertEqual(fs.read("x/a.txt"), "hello world")
            fs.copy("x/a.txt", "x/b.txt")
            fs.rename("x/b.txt", "x/c.txt")
            self.assertIn("c.txt", fs.list_dir("x"))
            fs.delete("x/c.txt")
            self.assertNotIn("c.txt", fs.list_dir("x"))

    def test_escape_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            fs = SandboxFS(Path(tmp))
            with self.assertRaises(ValueError):
                fs.safe_path("../outside")
            with self.assertRaises(ValueError):
                fs.safe_path("/etc/passwd")


if __name__ == "__main__":
    unittest.main()
