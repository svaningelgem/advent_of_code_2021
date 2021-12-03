from pathlib import Path

from _pytest.fixtures import fixture

from step2 import calculate_position, _read_data, calculate_position_with_aim

TEST_INPUT = Path(__file__).parent / 'step2.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step2.txt'


@fixture
def test_data():
    yield _read_data(TEST_INPUT)


@fixture
def real_data():
    yield _read_data(REAL_INPUT)


def test_step2(test_data):
    assert calculate_position(test_data) == 150


def test_step2_real_data(real_data):
    assert calculate_position(real_data) == 2039256


def test_step2_part2(test_data):
    assert calculate_position_with_aim(test_data) == 900


def test_step2_part2_real_data(real_data):
    assert calculate_position_with_aim(real_data) == 1856459736
