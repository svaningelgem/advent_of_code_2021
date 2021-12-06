
from pathlib import Path

from _pytest.fixtures import fixture

TEST_INPUT = Path(__file__).parent / 'step13.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step13.txt'


def test_step13():
    # assert calculate_position() == 150
    pass


def test_step13_real_data():
    # assert calculate_position() == 2039256
    pass


def test_step13_part2():
    # assert calculate_position_with_aim() == 900
    pass


def test_step13_part2_real_data():
    # assert calculate_position_with_aim() == 1856459736
    pass
