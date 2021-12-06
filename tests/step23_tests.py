
from pathlib import Path

from _pytest.fixtures import fixture

TEST_INPUT = Path(__file__).parent / 'step23.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step23.txt'


def test_step23():
    # assert calculate_position() == 150
    pass


def test_step23_real_data():
    # assert calculate_position() == 2039256
    pass


def test_step23_part2():
    # assert calculate_position_with_aim() == 900
    pass


def test_step23_part2_real_data():
    # assert calculate_position_with_aim() == 1856459736
    pass
