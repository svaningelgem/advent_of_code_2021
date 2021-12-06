from pathlib import Path

from _pytest.fixtures import fixture
from step1 import _get_numbers, count_increases, count_sliding_window_increases

TEST_INPUT = Path(__file__).parent / 'step1.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step1.txt'


@fixture
def test_data():
    yield _get_numbers(TEST_INPUT)


@fixture
def real_data():
    yield _get_numbers(REAL_INPUT)


def test_part1(test_data):
    assert count_increases(test_data) == 7


def test_part1_real_data(real_data):
    assert count_increases(real_data) == 1696


def test_part2_sliding(test_data):
    assert count_increases(count_sliding_window_increases(test_data)) == 5


def test_part2_real_data(real_data):
    assert count_increases(count_sliding_window_increases(real_data)) == 1737
