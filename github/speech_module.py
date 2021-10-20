FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = []
    assert 0 < number < 1000, 'number is out of supported range (1-999)'
    if 100 <= number < 1000:
        result.append(FIRST_TEN[(number // 100) - 1])
        result.append(HUNDRED)
        number = number % 100
    if 20 <= number <= 99:
        result.append(OTHER_TENS[(number // 10) - 2])
        number = number % 10
    elif 10 <= number <= 19:
        result.append(SECOND_TEN[number - 10])
        number = 0
    if 1 <= number <= 9:
        result.append(FIRST_TEN[number - 1])
    return ' '.join(result)


if __name__ == '__main__':
    print(checkio(101))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
