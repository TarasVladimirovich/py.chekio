from typing import List, Tuple
import math


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    def inter(a, b):
        return abs(a[2] - b[2]) < math.dist(a[:2], b[:2]) < a[2] + b[2]

    groups = set()
    for circle in circles:
        connected = {g for g in groups if any(inter(c, circle) for c in g)}
        new_group = frozenset((circle,)).union(*connected)
        groups = groups.difference(connected) | {new_group}
    return len(groups)


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
