"""Puzzle 03-1 for advent of code 2022.
"""


def get_wrong_item_priority_sum(file_path: str) -> int:
    """Calculates the sum of the priorities for the misplaced items.

    Arguments:
        - file_path: the path to the file with the data.

    Returns:
        The sum of the priorities.
    """

    priority_sum = 0
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open(file_path, "r", encoding="utf-8") as file:
        backpacks = file.read().strip().split("\n")

    for backpack in backpacks:
        comp1, comp2 = backpack[:len(backpack)//2], \
            backpack[len(backpack)//2:]
        wrong_item = [item for item in comp1 if item in comp2][0]
        priority_sum += items.index(wrong_item) + 1

    return priority_sum


if __name__ == "__main__":
    print("Example:", get_wrong_item_priority_sum("03/example_03.txt"))
    print("Solution:", get_wrong_item_priority_sum("03/input_03.txt"))
