#
# tmp = [1, 1, 4, 4, 4, "hello", "hello", 4]
# print(tmp.count(4))
# exit()


def group_equal(els):
    if not els:
        return els
    ans = []
    n = 0
    for i in range(1, len(els)):
        if els[i - 1] != els[i]:
            ans.append(els[n:i])
            n = i
    ans.append(els[n:len(els)])
    return ans


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    # assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    # assert group_equal([1]) == [[1]]
    # assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
