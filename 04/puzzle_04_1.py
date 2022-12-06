"""Puzzle 04-1 for advent of code 2022.
"""


def get_contain_amount(file_path: str) -> int:
    """Gets the amount of pairs with section assignments where one
    fully contain the other.

    Arguments:
        - file_path: the path to the file with the section assigns.

    Returns:
        The amount of sections that fully contain each other.
    """
    amount = 0

    with open(file_path, "r", encoding="utf-8") as file:
        pairs = file.read().strip().split("\n")

    for pair in pairs:
        assignment1, assignment2 = pair.split(",")
        start1, end1 = map(int, assignment1.split("-"))
        start2, end2 = map(int, assignment2.split("-"))
        if start1 >= start2 and end1 <= end2:
            amount += 1
        elif start2 >= start1 and end2 <= end1:
            amount += 1

    return amount


if __name__ == "__main__":
    print("Example:", get_contain_amount("04/example_04.txt"))
    print("Solution:", get_contain_amount("04/input_04.txt"))
