from pathlib import Path

from step07 import _get_fuel_cost, find_least_fuel_position

TEST_INPUT = Path(__file__).parent / 'step07.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step07.txt'


def test_step7():
    assert find_least_fuel_position(TEST_INPUT) == 37


def test_step7_real_data():
    assert find_least_fuel_position(REAL_INPUT) == 341534


def test_step7_part2():
    assert _get_fuel_cost(16, 5, True) == 66
    assert find_least_fuel_position(TEST_INPUT, True) == 168


def test_step7_part2_real_data():
    assert find_least_fuel_position(REAL_INPUT, True) == 93397632
