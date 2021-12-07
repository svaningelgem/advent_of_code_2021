from functools import lru_cache
from pathlib import Path
from typing import List


def _getnumbers(file: Path) -> List[int]:
    return [
        int(x)
        for x in file.read_text().split(',')
    ]


@lru_cache(3000)
def _get_fuel_cost(from_: int, to_: int, exponential: bool) -> int:
    min_ = min(from_, to_)
    max_ = max(from_, to_)

    if exponential:
        return sum(
            (i - min_)
            for i in range(min_, max_+1)
        )
    else:
        return max_ - min_


def _what_if_move_all_to(lst: List[int], to_position: int, exponential: bool = False) -> int:
    fuel_cost = 0
    for entry in lst:
        fuel_cost += _get_fuel_cost(entry, to_position, exponential)
    return fuel_cost


def find_least_fuel_position(file: Path, exponential: bool = False) -> int:
    nrs = _getnumbers(file)
    min_ = min(nrs)
    max_ = max(nrs)

    return min(
        _what_if_move_all_to(nrs, i, exponential)
        for i in range(min_, max_+1)
    )
