from pathlib import Path

from step4 import BingoSystem

TEST_INPUT = Path(__file__).parent / 'step4.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step4.txt'


def test_step4():
    assert BingoSystem(TEST_INPUT).find_winning_bord() == 4512


def test_step4_real_data():
    assert BingoSystem(REAL_INPUT).find_winning_bord() == 38913


def test_step4_part2():
    assert BingoSystem(TEST_INPUT).find_loosing_bord() == 1924


def test_step4_part2_real_data():
    assert BingoSystem(REAL_INPUT).find_loosing_bord() == 16836
