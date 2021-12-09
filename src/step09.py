from pathlib import Path
from collections import namedtuple
from pathlib import Path
from typing import Generator, List

LowPoint = namedtuple('LowPoint', 'x y value')


def _is_low_point_protected(matrix: List[List[int]], x: int, y: int, x2: int, y2: int) -> bool:
    if x2 < 0 or y2 < 0:
        return True

    try:
        return matrix[y][x] < matrix[y2][x2]
    except (KeyError, IndexError):
        return True


def _is_a_9(matrix: List[List[int]], x: int, y: int) -> bool:
    try:
        return matrix[y][x] == 9
    except (KeyError, IndexError):
        return True  # Borders also considered to be a 9


def _is_low_point(matrix: List[List[int]], x: int, y: int) -> bool:
    return (
        _is_low_point_protected(matrix, x, y, x, y - 1)
        and _is_low_point_protected(matrix, x, y, x, y + 1)
        and _is_low_point_protected(matrix, x, y, x - 1, y)
        and _is_low_point_protected(matrix, x, y, x + 1, y)
    )


def _get_matrix(file: Path) -> List[List[int]]:
    return [
        [int(c) for c in line]
        for line in file.read_text().splitlines()
    ]


def _find_all_lowest_points(matrix: List[List[int]]) -> Generator[LowPoint, None, None]:
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if _is_low_point(matrix, x, y):
                yield LowPoint(x, y, matrix[y][x])


def find_low_points(file: Path) -> int:
    matrix = _get_matrix(file)

    low_points = list(_find_all_lowest_points(matrix))

    return sum(x.value for x in low_points) + len(low_points)


def _find_basin_for(matrix: List[List[int]], x: int, y: int, final: List[LowPoint]) -> None:
    # A basin flows from the x,y position of the lowest point, and is bordered by 9's (not inclusive)
    if x < 0 or y < 0:
        return
    if _is_a_9(matrix, x, y):
        return  # Final step
    if any(x == pt.x and y == pt.y for pt in final):
        return  # Already been here.

    # Add field
    final.append(LowPoint(x, y, matrix[y][x]))

    # And branch outwards
    _find_basin_for(matrix, x - 1, y, final)
    _find_basin_for(matrix, x + 1, y, final)
    _find_basin_for(matrix, x, y - 1, final)
    _find_basin_for(matrix, x, y + 1, final)


def find_basins(file: Path) -> int:
    matrix = _get_matrix(file)

    low_points = list(_find_all_lowest_points(matrix))

    # For each low point: find the basin it is in.
    all_basins = []
    for lp in low_points:
        final = []
        _find_basin_for(matrix, lp.x, lp.y, final)
        all_basins.append(final)

    all_basins = sorted(all_basins, key=len)

    return len(all_basins[-1]) * len(all_basins[-2]) * len(all_basins[-3])
