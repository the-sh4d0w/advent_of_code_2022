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
        match round_[-1]:
            case "X":  # lost
                total_score += 0
                match round_[0]:
                    case "A":  # Rock -> Scissors
                        total_score += 3
                    case "B":  # Paper -> Rock
                        total_score += 1
                    case "C":  # Scissors -> Paper
                        total_score += 2
            case "Y":  # draw
                total_score += 3
                match round_[0]:
                    case "A":  # Rock -> Rock
                        total_score += 1
                    case "B":  # Paper -> Paper
                        total_score += 2
                    case "C":  # Scissors -> Scissors
                        total_score += 3
            case "Z":  # won
                total_score += 6
                match round_[0]:
                    case "A":  # Rock -> Paper
                        total_score += 2
                    case "B":  # Paper -> Scissors
                        total_score += 3
                    case "C":  # Scissors -> Rock
                        total_score += 1

    return total_score


if __name__ == "__main__":
    print("Example:", calculate_total_score("02/example_02.txt"))
    print("Solution:", calculate_total_score("02/input_02.txt"))
