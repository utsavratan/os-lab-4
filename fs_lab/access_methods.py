"""Sequential and direct file-access simulations."""


def sequential_access(records: list[str]) -> list[str]:
    print("\n=== SEQUENTIAL ACCESS ===")
    output = []
    for index, record in enumerate(records):
        print(f"READ record={index} -> {record!r}")
        output.append(record)
    return output


def direct_access(records: list[str], indexes: list[int]) -> list[str]:
    print("\n=== DIRECT ACCESS ===")
    output = []
    for index in indexes:
        if index < 0 or index >= len(records):
            raise IndexError(f"record {index} out of range")
        print(f"READ record={index} -> {records[index]!r}")
        output.append(records[index])
    return output


def demo() -> None:
    records = [f"Record-{i}" for i in range(8)]
    sequential_access(records)
    direct_access(records, [5, 1, 7, 2])
