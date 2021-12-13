from pathlib import Path

from step13 import fold_paper, print_letter

TEST_INPUT = Path(__file__).parent / 'step13.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step13.txt'


def test_step13():
    assert fold_paper(TEST_INPUT, 1) == 17
    assert fold_paper(TEST_INPUT, 2) == 16


def test_step13_real_data():
    assert fold_paper(REAL_INPUT, 1) == 671


def test_step13_part2():
    assert print_letter(TEST_INPUT) == """
#####
#...#
#...#
#...#
#####
""".strip()


def test_step13_part2_real_data():
    assert print_letter(REAL_INPUT) == """
###...##..###..#..#..##..###..#..#.#...
#..#.#..#.#..#.#..#.#..#.#..#.#.#..#...
#..#.#....#..#.####.#..#.#..#.##...#...
###..#....###..#..#.####.###..#.#..#...
#....#..#.#....#..#.#..#.#.#..#.#..#...
#.....##..#....#..#.#..#.#..#.#..#.####
""".strip()
