from itertools import zip_longest

def checkio(text, word):
    q = text.strip().replace(' ', '').split('\n')
    horizontal = text.strip().replace(' ', '').replace('\n', '')
    result = []
    print(horizontal)
    if word in horizontal:
        for n, line in enumerate(q, 1):
            if word in line.lower():
                start = line.lower().find(word) + 1
                end = start + len(word) - 1
                result = [n, start, n, end]
    else:
        tmp = []
        for n, i in enumerate(q[0]):
            inner = ''
            for j in q:
                try:
                    inner += j[n]
                except IndexError:
                    continue
            tmp.append(inner)
        for n, line in enumerate(tmp, 1):
            if word in line.lower():
                start = line.lower().find(word) + 1
                end = start + len(word) - 1
                print([start, n, end, n])
                result = [start, n, end, n]
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("xa\nxb\nx","ab"))

#     assert checkio("""DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?""", "ten") == [2, 14, 2, 16]
#     assert checkio("""He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
