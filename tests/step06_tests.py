
from pathlib import Path

from step06 import simulate_life

TEST_INPUT = Path(__file__).parent / 'step06.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step06.txt'


def test_step6():
    school = simulate_life(TEST_INPUT, 18)
    assert len(school) == 26

    school = simulate_life(TEST_INPUT, 80)
    assert len(school) == 5934


def test_step6_real_data():
    school = simulate_life(REAL_INPUT, 80)
    assert len(school) == 372300


def test_step6_part2():
    school = simulate_life(TEST_INPUT, 256)
    assert len(school) == 26984457539


def test_step6_part2_real_data():
    school = simulate_life(REAL_INPUT, 256)
    assert len(school) == 1675781200288
