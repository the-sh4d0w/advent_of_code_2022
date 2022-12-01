"""Puzzle 01-1 for advent of code 2022.
"""


def find_max_calories(file_path: str) -> int:
    """Searches the input textfile for the maximum number of calories.

    Arguments:
        - file_path: the path to the input file.

    Returns:
        The maximum number of calories.
    """
    max_calories = 0

    with open(file_path, "r", encoding="utf-8") as file:
        calories_list = file.read().split("\n\n")

    for calories in calories_list:
        if (current_calories := sum(map(int, calories.split()))) \
                > max_calories:
            max_calories = current_calories

    return max_calories


if __name__ == "__main__":
    print("Example:", find_max_calories("01/example_01.txt"))
    print("Solution:", find_max_calories("01/input_01.txt"))
