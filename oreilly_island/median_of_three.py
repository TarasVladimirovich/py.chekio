from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    if len(els) <= 2:
        return els[:2]
    tmp = els[:2]
    for i in range(3, len(els)+1):
        tmp.append(sorted(els[i-3:i])[1])
    return tmp


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([5, 2, 9, 1, 7, 4, 6, 3, 8]))) # [5,2,5,2,7,4,6,4,6]
    print(list(median_three([5, 2])))
    print(list(median_three([-1, 0, 1])))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    # assert list(median_three([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
