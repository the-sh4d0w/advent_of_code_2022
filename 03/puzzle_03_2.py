"""Puzzle 03-2 for advent of code 2022.
"""


def get_badge_priority_sum(file_path: str) -> int:
    """Calculates the sum of the priorities for the badges.

    Arguments:
        - file_path: the path to the file with the data.

    Returns:
        The sum of the priorities.
    """

    priority_sum = 0
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open(file_path, "r", encoding="utf-8") as file:
        backpacks = file.read().strip().split("\n")

    for index in range(0, len(backpacks), 3):
        backpack1, backpack2, backpack3 = backpacks[index], \
            backpacks[index+1], backpacks[index+2]
        badge = [item for item in backpack1
                 if item in backpack2 and item in backpack3][0]
        priority_sum += items.index(badge) + 1

    return priority_sum


if __name__ == "__main__":
    print("Example:", get_badge_priority_sum("03/example_03.txt"))
    print("Solution:", get_badge_priority_sum("03/input_03.txt"))
