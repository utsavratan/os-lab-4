import unittest
from fs_lab.permissions import PermissionSet, check


class PermissionTests(unittest.TestCase):
    def test_owner(self):
        p = PermissionSet(owner="rw-", group="r--", other="---")
        self.assertTrue(check(p, "owner", "read"))
        self.assertTrue(check(p, "owner", "write"))

    def test_denied(self):
        p = PermissionSet(owner="rw-", group="r--", other="---")
        self.assertFalse(check(p, "other", "write"))


if __name__ == "__main__":
    unittest.main()
