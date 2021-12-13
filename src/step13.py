from dataclasses import dataclass
from pathlib import Path


@dataclass
class FoldLine:
    direction: str
    coordinate: int

    def __post_init__(self):
        self.direction = self.direction.strip()
        self.coordinate = int(self.coordinate)


@dataclass
class Point:
    x: int
    y: int


class Paper:
    def _load_file(self, file: Path):
        self.points = []
        self.folds = []
        for line in file.read_text().splitlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith('fold along'):
                self.folds.append(FoldLine(*line[11:].split('=')))
            else:
                self.points.append(Point(*map(int, line.split(','))))

    def __init__(self, file: Path):
        self._load_file(file)

    def fold(self, folds: int):
        folds = self.folds if folds == -1 else self.folds[:folds]

        for fold in folds:
            if fold.direction == 'y':
                self._fold_upwards(fold.coordinate)
            elif fold.direction == 'x':
                self._fold_sidewards(fold.coordinate)
            else:
                raise ValueError("Invalid fold")

    def _remove_duplicates(self):
        new = []
        for pt in self.points:
            if pt not in new:
                new.append(pt)

        self.points = new

    def _fold_upwards(self, coordinate):
        for i in range(coordinate):
            source = coordinate * 2 - i
            for pt in self.points:
                if pt.y == source:
                    pt.y = i

        self._remove_duplicates()

    def _fold_sidewards(self, coordinate):
        for i in range(coordinate):
            source = coordinate * 2 - i
            for pt in self.points:
                if pt.x == source:
                    pt.x = i

        self._remove_duplicates()

    def __str__(self):
        max_x = max(pt.x for pt in self.points)
        max_y = max(pt.y for pt in self.points)
        array = [
            ['.' for _ in range(max_x+1)]
            for _ in range(max_y+1)
        ]
        for pt in self.points:
            array[pt.y][pt.x] = '#'
        return '\n'.join(
            ''.join(line)
            for line in array
        ).strip()


def _fold_paper(file: Path, folds: int) -> Paper:
    paper = Paper(file)
    paper.fold(folds)

    return paper


def fold_paper(file: Path, folds: int) -> int:
    return len(_fold_paper(file, folds).points)


def print_letter(file: Path) -> str:
    paper = _fold_paper(file, -1)
    return str(paper)
