from pathlib import Path

from step5 import load_field

TEST_INPUT = Path(__file__).parent / 'step5.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step5.txt'


def test_step5():
    field = load_field(TEST_INPUT)
    assert field.display() == '''.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
'''
    assert field.dangerous_points == 5


def test_step5_real_data():
    assert load_field(REAL_INPUT).dangerous_points == 7142


def test_step5_part2():
    field = load_field(TEST_INPUT, False)
    assert field.display() == '''1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
'''
    assert field.dangerous_points == 12


def test_step5_part2_real_data():
    assert load_field(REAL_INPUT, False).dangerous_points == 20012
