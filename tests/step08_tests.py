
from pathlib import Path

from step08 import _get_number, decipher_line, decode_numbers

TEST_INPUT = Path(__file__).parent / 'step08.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step08.txt'


def test_step8():
    assert decipher_line(TEST_INPUT) == 26


def test_step8_real_data():
    assert decipher_line(REAL_INPUT) == 488


def test_step8_part2():
    assert _get_number('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf') == 5353
    assert decode_numbers(TEST_INPUT) == 61229


def test_step8_part2_real_data():
    assert decode_numbers(REAL_INPUT) == 1040429
