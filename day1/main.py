from pathlib import Path


def determine_total_calories(package: list[int]) -> int:
    return sum(package)


def find_top_n_elves(packages: list[list[int]], n: int) -> int:
    top_n_elves = [0] * n
    for package in packages:
        calories = determine_total_calories(package)
        if any([calories > package for package in top_n_elves]):
            top_n_elves.pop(top_n_elves.index(min(top_n_elves)))
            top_n_elves.append(calories)
    return sum(top_n_elves)


def find_max_calories_package(packages: list[list[int]]) -> int:
    max_calories_package = 0
    for package in packages:
        if (calories := determine_total_calories(package)) > max_calories_package:
            max_calories_package = calories
    return max_calories_package


def get_packages_from_file(file: str) -> list[list[int]]:
    elves_carrying_packages = []
    with open(str(Path(__file__).parent / file), "r") as f:
        last_beginning = 0
        lines = f.readlines()
        for index, line in enumerate(lines):
            if not line.strip():
                elves_carrying_packages.append(
                    [int(value) for value in lines[last_beginning:index]]
                )
                last_beginning = index + 1
    return elves_carrying_packages


if __name__ == "__main__":
    print(find_top_n_elves(get_packages_from_file("input.txt"), n=3))
