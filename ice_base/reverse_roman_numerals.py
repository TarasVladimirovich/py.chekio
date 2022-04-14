ROMAN = {'I': 1, 'V': 5, 'X': 10,
         'L': 50, 'C': 100,
         'D': 500, 'M': 1000}


def reverse_roman(roman_string):
    sum_ = 0
    for i in range(1, len(roman_string) + 1):
        if i < len(roman_string) and ROMAN[roman_string[i]] > ROMAN[roman_string[i - 1]]:
            sum_ -= ROMAN[roman_string[i - 1]]
            continue
        sum_ += ROMAN[roman_string[i - 1]]
    return sum_

# def reverse_roman(s):
#     int_val = 0
#     for i in range(len(s)):
#         if i > 0 and ROMAN[s[i]] > ROMAN[s[i - 1]]:
#             int_val += ROMAN[s[i]] - 2 * ROMAN[s[i - 1]]
#         else:
#             int_val += ROMAN[s[i]]
#     return int_val

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(reverse_roman('V'))
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('V') == 5, '5'
    assert reverse_roman('III') == 3, '3'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
#     print('Great! It is time to Check your code!');
