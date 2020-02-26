# import math
# n = 1024000
# print(len(str(n)))
# # print(math.trunc(n))
#
# exit()

import math


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    count = 0
    tmp = number
    bre = len(powers)
    while abs(tmp) >= base:
        if bre == 1:
            break
        tmp /= base
        count +=1
        bre -= 1
    number = number/(base**count)
    if decimals == 0:
        number = math.trunc(number)
    return f"{number:.{decimals}f}{powers[count]}{suffix}"


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(friendly_number(42, powers=["u","d"], suffix="-n"))
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(255000000000, decimals=0, powers=['', 'k', 'M']) == '255000M', '255000M'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    # print("complete")




