
from pathlib import Path

from _pytest.fixtures import fixture

TEST_INPUT = Path(__file__).parent / 'step10.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step10.txt'


def test_step10():
    # assert calculate_position() == 150
    pass


def test_step10_real_data():
    # assert calculate_position() == 2039256
    pass


def test_step10_part2():
    # assert calculate_position_with_aim() == 900
    pass


def test_step10_part2_real_data():
    # assert calculate_position_with_aim() == 1856459736
    pass
