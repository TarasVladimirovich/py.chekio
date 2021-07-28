

def count_consecutive_summers(num):
    count = 0
    for i in range(1, num+1):
        sum = 0
        tmp = []
        for y in range(i, num+1):
            sum = sum + y
            tmp.append(y)
            if sum == num:
                count = count + 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_consecutive_summers(42) == 4
    # assert count_consecutive_summers(99) == 6
    # assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")