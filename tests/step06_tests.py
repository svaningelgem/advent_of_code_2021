
from pathlib import Path

from _pytest.fixtures import fixture

TEST_INPUT = Path(__file__).parent / 'step06.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step06.txt'


def test_step6(test_data):
    # assert calculate_position(test_data) == 150
    pass


def test_step6_real_data(real_data):
    # assert calculate_position(real_data) == 2039256
    pass


def test_step6_part2(test_data):
    # assert calculate_position_with_aim(test_data) == 900
    pass


def test_step6_part2_real_data(real_data):
    # assert calculate_position_with_aim(real_data) == 1856459736
    pass
