import operator
import re
from pathlib import Path
from typing import List, Optional


def load_field(filename, only_horizontal_and_vertical=True):
    field = Field(only_horizontal_and_vertical)

    for line in Path(filename).read_text().splitlines():
        field.add_line(line)

    return field


class Field:
    _field = None

    def __init__(self, only_horizontal_and_vertical=True):
        self.field = []
        self.only_horizontal_and_vertical = only_horizontal_and_vertical

    def _get_coords(self, line: str) -> Optional[List[int]]:
        line = line.strip()
        if not line:
            return None

        match = re.match(r'^\s*(\d+)\s*,\s*(\d+)\s*->\s*(\d+)\s*,\s*(\d+)\s*$', line)
        if not match:
            raise ValueError("Invalid line")

        return [int(x) for x in match.groups()]

    def add_line(self, line: str):
        x1, y1, x2, y2 = self._get_coords(line)
        if self.only_horizontal_and_vertical and not (x1 == x2 or y1 == y2):
            return  # Ignore this line...

        self._enlarge_height(max(y1, y2))
        self._enlarge_width(max(x1, x2))

        a = abs(x2 - x1)
        op_x = operator.add if x2 > x1 else operator.sub
        b = abs(y2 - y1)
        op_y = operator.add if y2 > y1 else operator.sub

        if x1 == x2 or y1 == y2:
            # Draw horizontal / vertical line.
            for a1 in range(a + 1):
                for b1 in range(b + 1):
                    self.field[op_y(y1, b1)][op_x(x1, a1)] += 1
        else:
            # Draw diagonal line
            assert a == b, "Diagonal line is not 45° exactly!"
            for i in range(a + 1):
                self.field[op_y(y1, i)][op_x(x1, i)] += 1

    @property
    def dangerous_points(self) -> int:
        return sum(
            1
            for line in self.field
            for el in line
            if el > 1
        )

    def display(self) -> str:
        disp = ''
        for line in self.field:
            disp += ''.join('.' if c == 0 else str(c) for c in line) + '\n'
        return disp

    def _enlarge_width(self, min_width):
        if self.field and min_width < len(self.field[0]):
            return

        for line in self.field:
            line.extend(0 for _ in range(min_width - len(line) + 1))

    def _enlarge_height(self, min_height):
        if min_height < len(self.field):
            return

        for _ in range(min_height - len(self.field) + 1):
            if self.field:
                self.field.append([0 for _ in range(len(self.field[0]))])
            else:
                self.field.append([])
