from pathlib import Path

from step12 import find_distinct_paths, find_multi_paths

TEST1_INPUT = Path(__file__).parent / 'step12_1.txt'
TEST2_INPUT = Path(__file__).parent / 'step12_2.txt'
TEST3_INPUT = Path(__file__).parent / 'step12_3.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step12.txt'


def test_step12():
    assert find_distinct_paths(TEST1_INPUT) == 10
    assert find_distinct_paths(TEST2_INPUT) == 19
    assert find_distinct_paths(TEST3_INPUT) == 226


def test_step12_real_data():
    assert find_distinct_paths(REAL_INPUT) == 5252


def test_step12_part2():
    assert find_multi_paths(TEST1_INPUT) == 36
    assert find_multi_paths(TEST2_INPUT) == 103
    assert find_multi_paths(TEST3_INPUT) == 3509


def test_step12_part2_real_data():
    assert find_multi_paths(REAL_INPUT) == 147784
