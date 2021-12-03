from pathlib import Path

from step1 import count_increases, count_sliding_window_increases

TEST_INPUT = Path(__file__).parent / 'step1.txt'
REAL_INPUT = Path(__file__).parent.parent.parent / 'src/step1.txt'


def test_part1():
    assert count_increases(TEST_INPUT) == 7


def test_part1_real_data():
    assert count_increases(REAL_INPUT) == 1696


def test_part2_sliding():
    assert count_increases(count_sliding_window_increases(TEST_INPUT)) == 5


def test_part2_real_data():
    assert count_increases(count_sliding_window_increases(REAL_INPUT)) == 1737

