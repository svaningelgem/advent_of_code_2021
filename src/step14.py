from collections import defaultdict
from pathlib import Path
from typing import Dict, Tuple


def _read_file(file: Path) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    first_line = None
    replacements = {}

    for line in file.read_text().splitlines():
        line = line.strip()
        if not line: continue

        if first_line is None:
            first_line = line
            continue

        from_, insertion = map(str.strip, line.split('->'))
        assert from_ not in replacements
        replacements[from_] = (from_[0] + insertion, insertion + from_[1])

    return first_line, replacements


def _split_polymer_in_parts(template) -> Dict[str, int]:
    tmp = defaultdict(int)
    for i in range(len(template)):
        part = template[i:i+2]
        if len(part) != 2: continue

        tmp[part] += 1
    return tmp


def _perform_insertions(file: Path, times: int = 10) -> Dict[str, int]:
    template, replacements = _read_file(file)

    current_state = _split_polymer_in_parts(template)

    for _ in range(times):
        previous_parts = [(k, v) for k, v in current_state.items() if v > 0]
        for part, amount in previous_parts:
            if part not in replacements: continue

            current_state[part] -= amount
            for repl in replacements[part]:
                current_state[repl] += amount

    return current_state


def _custom_count(template: Dict[str, int]) -> Dict[str, int]:
    counter = defaultdict(int)
    for idx, (k, v) in enumerate(template.items()):
        if idx == 0:  # Only count the first entry
            counter[k[0]] += v

        counter[k[1]] += v
    return counter


def count_least_most_after_insertions(file: Path, times: int) -> int:
    calculated_template = _perform_insertions(file, times)

    counter = _custom_count(calculated_template)

    return max(counter.values()) - min(counter.values())
