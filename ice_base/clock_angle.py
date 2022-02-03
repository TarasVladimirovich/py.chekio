def clock_angle(time):
    h, m = list(map(int, time.split(':')))
    if h >= 12:
        h = h - 12
    coefficient = m / 60
    res = abs(360 * coefficient - ((h * 30) + 30 * coefficient))
    if res > 180:
        return round(360 - res, 1)
    return res


if __name__ == '__main__':
    # print(clock_angle("2:30"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
