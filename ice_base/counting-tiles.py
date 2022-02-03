def checkio(radius):
    ran, solid, total = range(int(radius) + 1), 0, 0
    for x in ran:
        for y in ran:
            solid += abs(x + y * 1j + 1 + 1j) <= radius
            total += abs(x + y * 1j) < radius
    return [solid * 4, (total - solid) * 4]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
