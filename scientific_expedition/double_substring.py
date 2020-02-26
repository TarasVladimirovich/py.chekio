def double_substring(line):
    max = 0
    count = 0
    sting = ""
    for i in range(0, len(line)):
        if 2+count >= len(line):
            print(sting)
            return max
        tmp = line[0+count:2+count]
        tmp1 = line.count(tmp)
        if tmp1 > 1:
            if tmp1 > max:
                sting = tmp
                max = tmp1
            count += 1
        count += 1
    print(len(sting))
    return len(sting)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(double_substring('aghtfghkofgh'))
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')