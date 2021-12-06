from pathlib import Path
from typing import Union


class School:
    def __init__(self):
        self._internal: Dict[int, int] = {k: 0 for k in range(9)}

    def add_fish(self, start_number: Union[str, int]) -> None:
        self._internal[int(start_number)] += 1

    def advance_x_days(self, amount: int = 0) -> None:
        for _ in range(amount):
            new_school = {k - 1: v for k, v in self._internal.items()}

            new_school[6] += new_school[-1]
            new_school[8] = new_school[-1]
            del new_school[-1]

            self._internal = new_school

    def __len__(self) -> int:
        return sum(self._internal.values())

    def __str__(self) -> str:
        return str(self._internal)


def create_school(filename) -> School:
    school = School()

    for nr in filename.read_text().split(','):
        school.add_fish(nr)

    return school


def display_school(school: School):
    print(school)


def simulate_life(filename: Path, amount_of_days: int) -> School:
    school = create_school(filename)
    school.advance_x_days(amount_of_days)
    return school
