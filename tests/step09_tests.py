from pathlib import Path

from step09 import find_low_points, find_basins

TEST_INPUT = Path(__file__).parent / 'step09.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step09.txt'


def test_step9():
    assert find_low_points(TEST_INPUT) == 15


def test_step9_real_data():
    assert find_low_points(REAL_INPUT) == 486


def test_step9_part2():
    assert find_basins(TEST_INPUT) == 1134


def test_step9_part2_real_data():
    assert find_basins(REAL_INPUT) == 1059300
