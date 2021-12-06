from pathlib import Path


def _get_text(file):
    return Path(file).read_text().splitlines()


def _transpose(txt):
    yield from (
        ''.join(chars)
        for chars in zip(*txt)
    )


def _reverse_bits(txt):
    return ''.join('1' if c == '0' else '0' for c in txt)


def _most_present_bit(txt: str) -> str:
    return '1' if txt.count('1') >= txt.count('0') else '0'


def _least_present_bit(txt: str) -> str:
    return '0' if txt.count('1') >= txt.count('0') else '1'


def calculate_gamma_epsilon(file) -> int:
    generator = _transpose(_get_text(file))

    gamma = ''.join(
        _most_present_bit(line)
        for line in generator
    )

    epsilon = _reverse_bits(gamma)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def _calculate_oxygen_co2(lines, func) -> str:
    oxygen = ''
    reduced_lines = lines.copy()
    for i in range(len(lines[0])):
        if len(reduced_lines) == 1:
            return reduced_lines[0]

        transposed_lines = list(_transpose(reduced_lines))
        bit = func(transposed_lines[i])

        oxygen += bit
        reduced_lines = [
            line
            for line in reduced_lines
            if line.startswith(oxygen)
        ]

    return oxygen


def calculate_oxygen_co2(file) -> int:
    lines = list(_get_text(file))

    # We need to do this len(lines[0]) times
    oxygen = _calculate_oxygen_co2(lines, _most_present_bit)
    co2 = _calculate_oxygen_co2(lines, _least_present_bit)

    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)

    return oxygen * co2
