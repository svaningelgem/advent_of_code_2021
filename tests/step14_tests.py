
from pathlib import Path

from _pytest.fixtures import fixture

TEST_INPUT = Path(__file__).parent / 'step14.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step14.txt'


def test_step14():
    # assert calculate_position() == 150
    pass


def test_step14_real_data():
    # assert calculate_position() == 2039256
    pass


def test_step14_part2():
    # assert calculate_position_with_aim() == 900
    pass


def test_step14_part2_real_data():
    # assert calculate_position_with_aim() == 1856459736
    pass
