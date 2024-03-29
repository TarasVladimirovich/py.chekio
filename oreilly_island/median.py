from typing import List


def checkio(data: List[int]) -> [int, float]:
    length = len(data)
    sdata = sorted(data)
    if len(data) % 2 != 0:
        return sdata[int(length / 2)]
    else:
        return (sdata[round(length / 2) -1] + sdata[round(length / 2)]) / 2


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
