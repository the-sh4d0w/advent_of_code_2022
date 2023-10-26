"""Puzzle 05-1 for advent of code 2022.
(https://adventofcode.com/2022/day/5)
"""


def get_stacks(crates: str) -> dict[str, list[str]]:
    """Extracts stacks from the input text.
    NEEDS TO BE REWORKED!

    Arguments:
        - crates: the crates in text form.

    Returns:
        The stacks representing the text.
    """
    amount_stacks = int(crates[-2])
    stacks = {str(i+1): [] for i in range(amount_stacks)}
    for line in crates.split("\n")[:-1][::-1]:
        for i in range(amount_stacks):
            j = (i * 3) + i
            crate = line[j+1:j+2]
            if crate != " ":
                stacks[str(i+1)].append(crate)
    return stacks


def get_top_crates(file_path: str) -> str:
    """Finds out which crates will be at the top of the stacks after
    rearrangement.

    Arguments:
        - file_path: the path to the file with the data.

    Returns:
        The top crates from left to right.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        crates, procedure = file.read().split("\n\n")

    stacks = get_stacks(crates)

    for instruction in procedure.split("\n"):
        amount, from_, to = instruction.split()[1::2]
        for _ in range(int(amount)):
            stacks[to].append(stacks[from_].pop())

    return "".join([stacks[stack][-1] for stack in stacks])


if __name__ == "__main__":
    print("Example:", get_top_crates("05/example_05.txt"))
    print("Solution:", get_top_crates("05/input_05.txt"))
