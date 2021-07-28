def time_converter(time):
    time, part = time.split()
    h, m = time.split(':')
    if part == 'p.m.':
        if h != '12':
            h = str(int(h) + 12)
    if part == 'a.m.':
        if int(h) < 10:
            h = '0'+h
        if h == '12':
            h = '00'
    return f'{h}:{m}'
    # if h == '12':
    #     return f'{h}:{m}'
    # if part == 'p.m.':
    #     return f'{int(h)+12}:{m}'
    # else:


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert time_converter('12:30 p.m.') == '12:30'
    # assert time_converter('9:00 a.m.') == '09:00'
    # assert time_converter('11:15 p.m.') == '23:15'
    # print("Coding complete? Click 'Check' to earn cool rewards!")