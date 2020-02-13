from typing import List


def checkio(game_result: List[str]) -> str:
    tmp3 = set()
    tmp4 = set()

    for i in range(3):
        tmp = set(game_result[i])
        tmp1 = set()

        for y in range(3):
            tmp1.add(game_result[y][i])
            tmp4.add(game_result[i][2-i])
            if i == y:
                tmp3.add(game_result[i][y])

        if len(tmp1) == 1:
            if list(tmp1)[0] == ".":
                continue
            return list(tmp1)[0]

        if len(tmp) == 1:
            if list(tmp)[0] == ".":
                continue
            return list(tmp)[0]

    if len(tmp3) == 1:
        if list(tmp3)[0] == ".":
            return "D"
        return list(tmp3)[0]
    if len(tmp4) == 1:
        if list(tmp4)[0] == ".":
            return "D"
        return list(tmp4)[0]
    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))


    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")