from pathlib import Path
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Union


class Node:
    def __init__(self, name: str):
        self.name = name
        self.is_big = name.isupper()
        self.connections: Set[Node] = set()

    def __eq__(self, other: Union[str, 'Node']) -> bool:
        if isinstance(other, Node):
            return other.name == self.name
        elif isinstance(other, str):
            return other == self.name

        raise ValueError(f"Don't know how to compare with '{type(other)}'.")

    def __hash__(self):
        return hash(self.name)

    def add_connection(self, other: 'Node'):
        self.connections.add(other)

    def __repr__(self):
        return f'Node({self.name}) -> {",".join(sorted(x.name for x in self.connections))}'


class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}

    def add_path(self, beg: str, end: str) -> None:
        if beg not in self.nodes: self.nodes[beg] = Node(beg)
        if end not in self.nodes: self.nodes[end] = Node(end)

        self.nodes[beg].add_connection(self.nodes[end])
        self.nodes[end].add_connection(self.nodes[beg])

    def __repr__(self):
        return f'Graph({",".join(sorted(self.nodes))})'

    def __getitem__(self, item):
        return self.nodes[item]


def _build_graph(file: Path) -> Graph:
    g = Graph()

    for line in file.read_text().splitlines():
        line = line.strip()
        if not line: continue

        g.add_path(*line.split('-'))

    return g


def _find_candidates_distinct(start: Node, path_till_now: List) -> List[Node]:
    return [
        conn
        for conn in start.connections
        if conn.is_big or conn not in path_till_now
    ]


def _find_candidates_multi(start: Node, path_till_now: List) -> List[Node]:
    candidates = []
    for conn in start.connections:
        if conn.is_big:
            candidates.append(conn)
            continue

        if conn.name in ['start', 'end'] and conn in path_till_now:
            continue

        if conn.name not in path_till_now:
            candidates.append(conn)
            continue

        # a single small cave can be visited at most twice, and the remaining small caves can be visited at most once

        # conn is a small cave, and conn is in the pathlist, but has ANY small cave been visited twice?
        cnt = defaultdict(int)
        for node in path_till_now:
            if node.is_big: continue

            cnt[node.name] += 1

        if all(x <= 1 for x in cnt.values() ):
            candidates.append(conn)
            continue

    return candidates


def _go_one_step(start: Node, path_till_now: List, find_candidates) -> Set[List[Node]]:
    candidates = find_candidates(start, path_till_now)

    final = set()

    for candidate in candidates:
        tmp = path_till_now.copy() + [candidate]
        if candidate == 'end':
            final.add(tuple(tmp))
        else:
            final.update(_go_one_step(candidate, tmp, find_candidates))

    return final


def _dump_paths(paths: Set[List[Node]]):
    lines = sorted(
        ",".join(node.name for node in path)
        for path in paths
    )

    print("\n".join(lines))


def find_distinct_paths(file: Path) -> int:
    g = _build_graph(file)
    start = g['start']
    return len(_go_one_step(start, [start], _find_candidates_distinct))


def find_multi_paths(file: Path) -> int:
    g = _build_graph(file)
    start = g['start']
    result = _go_one_step(start, [start], _find_candidates_multi)
    # _dump_paths(result)
    return len(result)
