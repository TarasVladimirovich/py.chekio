from itertools import combinations


def is_balanced(t, _t=None):
    while t != _t:
        _t, t = t, t.replace('()', '').replace('{}', '').replace('[]', '')
    return not t


def remove_brackets(line):
    for i in range(len(line)):
        for m in combinations(range(len(line)), i):
            if is_balanced(cm := ''.join(k for j, k in enumerate(line) if j not in m)):
                return cm
    return ''


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
