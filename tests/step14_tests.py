from pathlib import Path

from step14 import count_least_most_after_insertions

TEST_INPUT = Path(__file__).parent / 'step14.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step14.txt'


def test_step14():
    assert count_least_most_after_insertions(TEST_INPUT, 0) == 1  # 'NNCB'
    assert count_least_most_after_insertions(TEST_INPUT, 1) == 1  # 'NCNBCHB'
    assert count_least_most_after_insertions(TEST_INPUT, 2) == 5  # 'NBCCNBBBCBHCB'
    assert count_least_most_after_insertions(TEST_INPUT, 3) == 7  # 'NBBBCNCCNBBNBNBBCHBHHBCHB'
    assert count_least_most_after_insertions(TEST_INPUT, 4) == 18  # 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'

    assert count_least_most_after_insertions(TEST_INPUT, 10) == 1588


def test_step14_real_data():
    assert count_least_most_after_insertions(REAL_INPUT, 10) == 2223


def test_step14_part2():
    assert count_least_most_after_insertions(TEST_INPUT, 40) == 2188189693529


def test_step14_part2_real_data():
    assert count_least_most_after_insertions(REAL_INPUT, 40) == 2566282754493
