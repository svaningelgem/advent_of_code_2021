import sys
from pathlib import Path
from typing import Generator, Union


class SlidingWindow(list):
    max_size = 3

    def append(self, obj):
        super().append(obj)
        if len(self) > self.max_size:
            self.pop(0)

    @property
    def full(self) -> bool:
        return len(self) == self.max_size


def _get_numbers(file: Union[str, Path]) -> Generator[int, None, None]:
    yield from (
        int(line.strip())
        for line in Path(file).read_text().splitlines()
        if line.strip()
    )


def count_increases(generator):
    pre = sys.maxsize

    count = 0
    for x in generator:
        if pre < x:
            count += 1

        pre = x

    return count


def count_sliding_window_increases(generator):
    bucket = SlidingWindow()

    for x in generator:
        bucket.append(x)
        if bucket.full:
            yield sum(bucket)


if __name__ == '__main__':
    file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

    count = count_increases(_get_numbers(file))
    print("increases:", count)
    count = count_increases(count_sliding_window_increases(file))
    print('sliding increase:', count)
