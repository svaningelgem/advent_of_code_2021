from collections import namedtuple
from pathlib import Path
from typing import Union, Generator

Movement = namedtuple('Movement', 'direction amount')


def _read_data(file: Union[str, Path]) -> Generator[Movement, None, None]:
    for line in Path(file).read_text().splitlines():
        if not line.strip():
            continue

        tmp = line.split(' ')
        yield Movement(tmp[0], int(tmp[1]))


def calculate_position(generator: Generator[Movement, None, None]) -> int:
    horizontal = depth = 0

    for x in generator:
        if x.direction == 'forward':
            horizontal += x.amount
        elif x.direction == 'down':
            depth += x.amount
        elif x.direction == 'up':
            depth -= x.amount

    return horizontal * depth


def calculate_position_with_aim(generator: Generator[Movement, None, None]) -> int:
    horizontal = depth = aim = 0

    for x in generator:
        if x.direction == 'forward':
            horizontal += x.amount
            depth += aim * x.amount
        elif x.direction == 'down':
            aim += x.amount
        elif x.direction == 'up':
            aim -= x.amount

    return horizontal * depth
