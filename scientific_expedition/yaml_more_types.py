const = {'': None, 'null': None, 'true': True, 'false': False}


def convert(value):
    if value in const:
        return const[value]
    if value.isdigit(): 
        return int(value)
    if value[0] in '"\'':
        return value[1:-1].encode('utf-8').decode('unicode_escape')
    return value


def yaml(a):
    res = {}
    for s in filter(None, a.splitlines()):
        key, value = s.split(':')
        res[key] = convert(value.strip())
    return res


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
