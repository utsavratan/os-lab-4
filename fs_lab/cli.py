"""Command-line interface for the filesystem practical."""

from __future__ import annotations
import argparse
from pathlib import Path
from . import __version__
from .real_fs import demo as real_demo
from .access_methods import demo as access_demo
from .directories import demo as directories_demo
from .allocation import demo as allocation_demo
from .free_space import demo as free_space_demo
from .permissions import demo as permissions_demo
from .simulated_fs import demo as simulated_demo


def build_parser():
    parser = argparse.ArgumentParser(
        prog="fs-lab",
        description="File-System Interface and Implementation Practical Lab",
    )
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("real", help="controlled real filesystem demonstration")
    sub.add_parser("access", help="sequential and direct access")
    sub.add_parser("directories", help="directory organization")
    sub.add_parser("allocation", help="file allocation methods")
    sub.add_parser("free-space", help="free-space management")
    sub.add_parser("permissions", help="permissions and access control")
    sub.add_parser("simulated", help="integrated simulated filesystem")
    sub.add_parser("all", help="run the complete practical")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    project_root = Path(__file__).resolve().parents[1]
    sandbox = project_root / "sandbox"

    if args.command == "real":
        real_demo(sandbox)
    elif args.command == "access":
        access_demo()
    elif args.command == "directories":
        directories_demo()
    elif args.command == "allocation":
        allocation_demo()
    elif args.command == "free-space":
        free_space_demo()
    elif args.command == "permissions":
        permissions_demo()
    elif args.command == "simulated":
        simulated_demo()
    elif args.command == "all":
        real_demo(sandbox)
        access_demo()
        directories_demo()
        allocation_demo()
        free_space_demo()
        permissions_demo()
        simulated_demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
