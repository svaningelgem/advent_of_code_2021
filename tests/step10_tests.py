from pathlib import Path

from step10 import autocomplete_score, find_score_part1

TEST_INPUT = Path(__file__).parent / 'step10.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step10.txt'


def test_step10():
    assert find_score_part1(TEST_INPUT) == 26397


def test_step10_real_data():
    assert find_score_part1(REAL_INPUT) == 318081


def test_step10_part2():
    assert autocomplete_score(TEST_INPUT) == 288957


def test_step10_part2_real_data():
    assert autocomplete_score(REAL_INPUT) == 4361305341
