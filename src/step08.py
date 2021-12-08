import itertools
from collections import Counter
from pathlib import Path
from typing import Set, Tuple

digits = [
    'abcefg',   # 0
    'cf',       # 1
    'acdeg',    # 2
    'acdfg',    # 3
    'bcdf',     # 4
    'abdfg',    # 5
    'abdefg',   # 6
    'acf',      # 7
    'abcdefg',  # 8
    'abcdfg',   # 9
]
d_0 = digits[0]
d_1 = digits[1]
d_2 = digits[2]
d_3 = digits[3]
d_4 = digits[4]
d_5 = digits[5]
d_6 = digits[6]
d_7 = digits[7]
d_8 = digits[8]
d_9 = digits[9]
easy_digits = {
    k: v
    for k, v in enumerate(digits)
    if len([x for x in digits if len(v) == len(x)]) == 1
}


def _diff(x: str, y: str) -> Tuple[str, str]:
    return (
        ''.join(set(x) - set(y)),
        ''.join(set(y) - set(x))
    )


def _get_one_letter_apart(digits):
    return {
        (x, y, _diff(x, y)[1])
        for x, y in itertools.permutations(digits, r=2)
        if not _diff(x, y)[0] and len(_diff(x, y)[1]) == 1
    }


def decipher_line(file: Path) -> int:
    unique_lengths = [len(v) for v in easy_digits.values()]

    count = 0
    for line in file.read_text().splitlines():
        last_part = line.split('|')[-1].strip().split(' ')
        for v in last_part:
            if len(v) in unique_lengths:
                count += 1
    return count


def _find_difference(tab, d1, d2) -> Set[str]:
    possibilities = set()

    for x, y in itertools.product(tab[d1], tab[d2]):
        z = _diff(x, y)
        if z[1] == '' and len(z[0]) == 1:
            possibilities.add(z[0])
        elif z[0] == '' and len(z[1]) == 1:
            possibilities.add(z[1])

    return possibilities


def _add_to_know(know, orig, conv):
    if orig not in know:
        know[orig] = conv
    else:
        know[orig].intersection_update(conv)



def _get_number(first: str, second: str) -> int:
    splitted_first = first.strip().split(' ')
    working = digits.copy()

    conversion_table = {
        orig: [d for d in splitted_first if len(d) == len(orig)]
        for orig in working
    }

    know = {}  # Original letter -> converted letter

    entries = 0
    while not(len(know) == 7 and all(len(x) == 1 for x in know.values())):  # 7 unique values.
        entries += 1

        # These are 1 letter apart
        for d1, d2, target_letter in _get_one_letter_apart(working):
            if not (d1 and d2 and target_letter):
                continue

            try:
                converted_letter = _find_difference(conversion_table, d1, d2)
            except KeyError:
                continue
            else:
                _add_to_know(know, target_letter, converted_letter)

        # update entries that have the same elements, and same length:
        for tpl, cnt in Counter(tuple(x) for x in know.values()).items():
            if cnt <= 1:
                continue
            if len(tpl) != cnt:  # For example (a,b) is twice there: we can remove these letters from all others.
                continue

            tpl = set(tpl)
            for orig, conversion in know.items():
                if conversion == tpl:
                    continue

                conversion.difference_update(tpl)

        # Now for the unique values: remove these from 'working'
        unique_values = {k: list(v)[0] for k, v in know.items() if len(v) == 1}

        # Create new conversion table:
        new_conversion_table = {}
        for k, v in conversion_table.items():
            new_key = ''.join(set(k) - set(unique_values.keys()))
            if new_key == '':
                continue

            new_values = [
                ''.join(set(old) - set(unique_values.values()))
                for old in v
            ]

            if len(new_key) == 1 and len(set(new_values)) == 1:
                _add_to_know(know, new_key, new_values[0])
                continue

            # Remove values that don't have the same length as the key anymore.
            new_conversion_table[new_key] = [x for x in new_values if len(x) == len(new_key)]
        conversion_table = new_conversion_table

        working = [
            ''.join(set(old) - set(unique_values.keys()))
            for old in working
        ]

    translation_mapping = {list(v)[0]: k for k, v in know.items() if len(v) == 1}
    converted = ''
    for c in second:
        try:
            converted += translation_mapping[c]
        except KeyError:
            converted += ' '
    converted = [''.join(sorted(x)) for x in converted.strip().split(' ') if x]
    final_number = ''.join(str(digits.index(x)) for x in converted)
    return int(final_number)


def decode_numbers(file: Path) -> int:
    lines = file.read_text().splitlines()
    total = 0
    for line in lines:  # type: str
        total += _get_number(*line.split('|'))
    return total