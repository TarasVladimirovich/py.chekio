from typing import Tuple


def follow(instructions: str) -> tuple[int, ...]:
    # print((instructions.count('r') - instructions.count('l'),
    #        instructions.count('f') - instructions.count('b')))

    # result = [0, 0]
    # for i in instructions:
    #     if i == 'f':
    #         result[1] += 1
    #     if i == 'b':
    #         result[1] -= 1
    #     if i == 'l':
    #         result[0] -= 1
    #     if i == 'r':
    #         result[0] += 1
    return (instructions.count('r') - instructions.count('l'),
           instructions.count('f') - instructions.count('b'))


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
#
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
