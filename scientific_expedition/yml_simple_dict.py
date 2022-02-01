def yaml(a):
    tmp = a.split('\n')
    d = {}
    for x in tmp:
        if not x:
            continue
        k, v = map(str.strip, x.split(':'))
        d[k] = int(v) if v.isdigit() else v
    return d


if __name__ == '__main__':
    #     print("Example:")
    #     print(yaml("""name: Alex
    # age: 12"""))
    #
    #     # These "asserts" are used for self-checking and not for an auto-testing
    #     assert yaml("""name: Alex
    # age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
