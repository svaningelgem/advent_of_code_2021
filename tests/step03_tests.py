from pathlib import Path

from step3 import calculate_gamma_epsilon, calculate_oxygen_co2

TEST_INPUT = Path(__file__).parent / 'step3.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step3.txt'


def test_step3():
    assert calculate_gamma_epsilon(TEST_INPUT) == 198


def test_step3_real_data():
    assert calculate_gamma_epsilon(REAL_INPUT) == 693486


def test_step3_part2():
    assert calculate_oxygen_co2(TEST_INPUT) == 230


def test_step3_part2_real_data():
    assert calculate_oxygen_co2(REAL_INPUT) == 3379326
