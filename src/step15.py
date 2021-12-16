from pathlib import Path
from pathlib import Path
from typing import List, Tuple

import networkx as nx


def get_cave_step1(file: Path) -> List[str]:
    return [l for l in file.read_text().splitlines() if l.strip()]


def _increase_by_x(line: str, i: int) -> str:
    line = [int(x) for x in line]
    new_nrs = [
        x + i if x + i < 10
        else x + i - 9
        for x in line
    ]
    return ''.join(str(x) for x in new_nrs)


def get_cave_step2(file: Path) -> List[str]:
    small_cave = get_cave_step1(file)
    huge_cave = []

    # 1st step: copy to the right.
    for line in small_cave:
        final_line = ''
        for i in range(5):  # Need to duplicate this 4 more times now
            final_line += _increase_by_x(line, i)
        huge_cave.append(final_line)

    # Now we need to copy it downwards 5x
    first_cave_line = huge_cave.copy()
    for i in range(1, 5):
        for line in first_cave_line:
            huge_cave.append(_increase_by_x(line, i))

    return huge_cave


def _load_graph(cave: List[str]) -> Tuple[str, nx.Graph]:
    graph = nx.DiGraph()
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            # to the right:
            if x + 1 < len(cave[0]):
                graph.add_edge(f'{x},{y}', f'{x+1},{y}', weight=int(cave[y][x+1]))
            # to the left:
            if x > 0:
                graph.add_edge(f'{x},{y}', f'{x-1},{y}', weight=int(cave[y][x-1]))

            # down
            if y + 1 < len(cave):
                graph.add_edge(f'{x},{y}', f'{x},{y+1}', weight=int(cave[y+1][x]))
            # up
            if y > 0:
                graph.add_edge(f'{x},{y}', f'{x},{y-1}', weight=int(cave[y-1][x]))

    return f'{x},{y}', graph


def find_route_minimal_risk(cave: List[str]) -> int:
    stop, graph = _load_graph(cave)
    start = '0,0'
    # path_to_walk = nx.dijkstra_path_length(graph, start, stop)
    return nx.dijkstra_path_length(graph, start, stop)
