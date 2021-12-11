from pathlib import Path
from typing import Tuple, Union


class Octopus:
    def __init__(self, initial_value: Union[str, int]):
        self.value = int(initial_value)
        self.times_flashed = 0
        self.has_flashed_already = 0

    def increase(self):
        self.value += 1

    def step2_init(self):
        self.has_flashed_already = 0

    def flash(self):
        if self.value <= 9:
            return

        self.has_flashed_already += 1

    def step3(self):
        if self.has_flashed_already:
            self.times_flashed += 1
            self.value = 0
            self.has_flashed_already = 0

    def __repr__(self) -> str:
        return str(self.value)


class Field:
    def __init__(self, file: Path):
        self.field = [
            [Octopus(x) for x in line]
            for line in file.read_text().splitlines()
        ]
        self.start_flashing = False

    def _do_for_all_oktopi(self, method: str):
        for line in self.field:
            for okt in line:
                getattr(okt, method)()

    def step1(self):
        """
        First, the energy level of each octopus increases by 1.
        """
        self._do_for_all_oktopi('increase')

    def step2(self):
        """
        Then, any octopus with an energy level greater than 9 flashes. This increases the energy level
        of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes
        an octopus to have an energy level greater than 9, it also flashes. This process continues as
        long as new octopuses keep having their energy level increased beyond 9. (An octopus can only
        flash at most once per step.)
        """
        self._do_for_all_oktopi('step2_init')

        keep_flashing = True

        while keep_flashing:
            self._do_for_all_oktopi('flash')

            keep_flashing = False
            for y, line in enumerate(self.field):
                for x, okt in enumerate(line):
                    if okt.has_flashed_already == 1:
                        self._increase_neighbours(x, y)
                        keep_flashing = True

    def step3(self):
        """
        Finally, any octopus that flashed during this step has its energy level
          set to 0, as it used all of its energy to flash.
        """
        self._do_for_all_oktopi('step3')

    def _increase(self, x: int, y: int) -> None:
        if x < 0 or y < 0:
            return

        try:
            self.field[y][x].increase()
        except IndexError:
            pass

    def _increase_neighbours(self, x: int, y: int) -> None:
        self._increase(x - 1, y - 1)
        self._increase(x, y - 1)
        self._increase(x + 1, y - 1)

        self._increase(x - 1, y)
        self._increase(x - 1, y + 1)

        self._increase(x + 1, y)
        self._increase(x + 1, y + 1)

        self._increase(x, y + 1)

    def get_flashes(self) -> int:
        return sum(
            okt.times_flashed
            for line in self.field
            for okt in line
        )

    def __repr__(self) -> str:
        return '\n'.join(
            ''.join(str(okt.value) for okt in line)
            for line in self.field
        )

    def do_all_steps(self):
        self.step1()
        self.step2()
        self.step3()

    def did_all_oktopi_flash(self):
        return all(
            okt.value == 0
            for line in self.field
            for okt in line
        )


def simulate_steps(file: Path, steps=100) -> Tuple[int, str]:
    field = Field(file)

    for _ in range(steps):
        field.do_all_steps()

    return field.get_flashes(), str(field)


def find_synchronized_flash(file: Path) -> int:
    field = Field(file)

    step = 0
    while not field.did_all_oktopi_flash():
        step += 1
        field.do_all_steps()

    return step
