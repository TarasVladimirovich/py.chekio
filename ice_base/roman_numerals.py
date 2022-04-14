ROMAN = {1: 'I',
         5: 'V',
         10: 'X',
         50: 'L',
         100: 'C',
         500: 'D',
         1000: 'M'}


def checkio(data):
    mult = 10 ** (len(str(data)) - 1)
    sum = ''
    while mult != 0:
        num = int(data // mult)
        if num in [4, 9]:
            sum += ROMAN[mult]
            sum += ROMAN[(num + 1) * mult]
        if 1 <= num < 4 or 5 <= num < 9:
            t = 1 if num < 4 else 5
            tmp, num = num - t, t
            sum += ROMAN[num * mult]
            sum += tmp * ROMAN[mult]
        data = int(data % mult)
        mult /= 10
    return sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
