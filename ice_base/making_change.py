def checkio(price, denominations):
    table = [0] + [price + 1] * price
    for coin in denominations:
        for i in range(coin, price + 1):
            table[i] = min(table[i], table[i - coin] + 1)
    return table[price] if table[price] <= price else None


def checkio(price, denoms):
    sums = set()
    for number in range(1, price + 1):
        sums = {s + d for s in sums for d in denoms} or set(denoms)
        if price in sums:
            return number


if __name__ == '__main__':
    print("Example:")
    # print(checkio(8, [1, 3, 5]))
    # print(checkio(1, [3, 4, 5]))
    print(checkio(12, [1, 4, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(8, [1, 3, 5]) == 2
    # assert checkio(12, [1, 4, 5]) == 3
    # print('Done')
