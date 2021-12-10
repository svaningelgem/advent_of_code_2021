from pathlib import Path


class CorruptedLine(Exception):
    def __init__(self, char):
        self.char = char


class IncompleteLine(Exception):
    def __init__(self, expected):
        self.expected = expected


def process_line(line) -> None:
    seen = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>',
    }

    expected = []
    for idx, c in enumerate(line):
        if not expected or c in seen:
            expected.append(seen[c])
            continue

        if c == expected[-1]:
            expected.pop()
            continue

        raise CorruptedLine(c)

    if expected:
        raise IncompleteLine(expected)


def find_score_part1(file: Path) -> int:
    score = 0
    score_table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    for line in file.read_text().splitlines():
        try:
            process_line(line)
        except IncompleteLine:
            pass
        except CorruptedLine as ex:
            score += score_table[ex.char]

    return score


def autocomplete_score(file: Path) -> int:
    score_table = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    scores = []
    for line in file.read_text().splitlines():
        try:
            process_line(line)
        except CorruptedLine:
            pass
        except IncompleteLine as ex:
            tmp = 0
            for c in reversed(ex.expected):
                tmp *= 5
                tmp += score_table[c]
            scores.append(tmp)

    scores = sorted(scores)
    return scores[len(scores) // 2]
