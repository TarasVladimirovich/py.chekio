def isometric_strings(a, b):
    # your code here
    print(set(zip(a, b)))
    print(len(set(zip(a, b))), len(set(a)))
    print(len(set(zip(a, b))) == len(set(a)))
    return len(set(zip(a, b))) == len(set(a))


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("gogopy", "doodle"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")
