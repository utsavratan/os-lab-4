"""Unix-style simulated permission and access-control checks."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class PermissionSet:
    owner: str = "rw-"
    group: str = "r--"
    other: str = "---"

    def symbolic(self) -> str:
        return f"{self.owner}{self.group}{self.other}"

    def allowed(self, identity: str, operation: str) -> bool:
        if identity == "owner":
            mode = self.owner
        elif identity == "group":
            mode = self.group
        elif identity == "other":
            mode = self.other
        else:
            raise ValueError("identity must be owner, group or other")

        required = {"read": "r", "write": "w", "execute": "x"}.get(operation)
        if required is None:
            raise ValueError("operation must be read, write or execute")
        return required in mode


def check(perms: PermissionSet, identity: str, operation: str) -> bool:
    allowed = perms.allowed(identity, operation)
    print(
        f"ACCESS identity={identity:<5} operation={operation:<7} "
        f"mode={perms.symbolic()} -> {'ALLOW' if allowed else 'DENY'}"
    )
    return allowed


def demo() -> None:
    print("\n=== PERMISSIONS & ACCESS CONTROL ===")
    perms = PermissionSet(owner="rwx", group="r-x", other="---")
    print("MODE:", perms.symbolic())
    for identity, operation in [
        ("owner", "read"),
        ("owner", "write"),
        ("group", "read"),
        ("group", "write"),
        ("other", "read"),
        ("other", "execute"),
    ]:
        check(perms, identity, operation)
