"""Puzzle 02-1 for advent of code 2022.
"""


def calculate_total_score(file_path: str) -> int:
    """Calculates the total score for rounds in the input file.

    Arguments:
        - file_path: the path to the input file.

    Return:
        The total score.
    """
    total_score = 0

    with open(file_path, "r", encoding="utf-8") as file:
        rounds = file.read().strip().split("\n")

    for round_ in rounds:
        match round_:
            case "A X":  # Rock Rock -> draw
                total_score += 1 + 3
            case "A Y":  # Rock Paper -> won
                total_score += 2 + 6
            case "A Z":  # Rock Scissors -> lost
                total_score += 3 + 0
            case "B X":  # Paper Rock -> lost
                total_score += 1 + 0
            case "B Y":  # Paper Paper -> draw
                total_score += 2 + 3
            case "B Z":  # Paper Scissors -> won
                total_score += 3 + 6
            case "C X":  # Scissors Rock -> won
                total_score += 1 + 6
            case "C Y":  # Scissors Paper -> lost
                total_score += 2 + 0
            case "C Z":  # Scissors Scissors -> draw
                total_score += 3 + 3

    return total_score


if __name__ == "__main__":
    print("Example:", calculate_total_score("02/example_02.txt"))
    print("Solution:", calculate_total_score("02/input_02.txt"))
