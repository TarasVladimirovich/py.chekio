import time


def checkio(number):
    pigeons = 0
    count = 1
    while True:
        if number <= pigeons:
            return pigeons
        pigeons += count
        if number < pigeons:
            return number
        number -= pigeons
        count += 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(10))
    # assert checkio(1) == 1, "1st example"
    # assert checkio(2) == 1, "2nd example"
    # assert checkio(5) == 3, "3rd example"
    # assert checkio(10) == 6, "4th example"