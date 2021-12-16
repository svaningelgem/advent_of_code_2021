from pathlib import Path

from step15 import find_route_minimal_risk, get_cave_step1, get_cave_step2

TEST_INPUT = Path(__file__).parent / 'step15.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step15.txt'


def test_step15():
    assert find_route_minimal_risk(get_cave_step1(TEST_INPUT)) == 40


def test_step15_real_data():
    # 450 is too low
    assert find_route_minimal_risk(get_cave_step1(REAL_INPUT)) == 458


def test_step15_part2():
    assert find_route_minimal_risk(get_cave_step2(TEST_INPUT)) == 315


def test_step15_part2_real_data():
    assert find_route_minimal_risk(get_cave_step2(REAL_INPUT)) == 2800
