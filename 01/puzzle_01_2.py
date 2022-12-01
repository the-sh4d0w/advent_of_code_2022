"""Puzzle 01-2 for advent of code 2022.
"""


def find_top_three_max_calories(file_path: str) -> int:
    """Searches the input textfile for the top three maximum numbers
    of calories.

    Arguments:
        - file_path: the path to the input file.

    Returns:
        The sum of the top three maximum numbers of calories.
    """
    max_calories = [0, 0, 0]

    with open(file_path, "r", encoding="utf-8") as file:
        calories_list = file.read().split("\n\n")

    for index in range(3):
        for calories in calories_list:
            current_calories = sum(map(int, calories.split()))
            if (index == 0 or current_calories < max_calories[index - 1]) and \
                    current_calories > max_calories[index]:
                max_calories[index] = current_calories

    return sum(max_calories)


if __name__ == "__main__":
    print("Example:", find_top_three_max_calories("01/example_01.txt"))
    print("Solution:", find_top_three_max_calories("01/input_01.txt"))
