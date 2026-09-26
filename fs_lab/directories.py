"""Directory organization simulations."""


def single_level(names: list[str]) -> dict:
    directory = {}
    print("\n=== SINGLE-LEVEL DIRECTORY ===")
    for name in names:
        if name in directory:
            raise ValueError(f"duplicate name: {name}")
        directory[name] = f"file:{name}"
        print(f"CREATE /{name}")
    print("TREE:", list(directory))
    return directory


def two_level(users: dict[str, list[str]]) -> dict:
    result = {}
    print("\n=== TWO-LEVEL DIRECTORY ===")
    for user, names in users.items():
        result[user] = {}
        for name in names:
            result[user][name] = f"file:{name}"
            print(f"CREATE /{user}/{name}")
    for user, entries in result.items():
        print(f"  /{user}: {list(entries)}")
    return result


def tree_structure() -> dict:
    tree = {
        "home": {
            "utsav": {
                "documents": {"os.txt": None},
                "projects": {"fs_lab.py": None},
            }
        },
        "system": {
            "logs": {"kernel.log": None},
            "config": {"system.conf": None},
        },
    }

    print("\n=== TREE-STRUCTURED DIRECTORY ===")

    def walk(node: dict, prefix: str = ""):
        for name, child in node.items():
            print(f"{prefix}{name}/" if child is not None else f"{prefix}{name}")
            if isinstance(child, dict):
                walk(child, prefix + "  ")

    walk(tree)
    return tree


def demo() -> None:
    single_level(["a.txt", "b.txt", "c.txt"])
    two_level({"user1": ["a.txt", "b.txt"], "user2": ["a.txt", "c.txt"]})
    tree_structure()
