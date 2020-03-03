import re
tmp = []
t =('X...',
    '..X.',
    'X..X',
    '....')

for i in range(len(t)):
    for y in range(len(t[i])):
        if t[i][y] == "X":
            tmp.append((i,y))

print(tmp)


exit()


def recall_password(cipher_grille, ciphered_password):
    tmp = []
    for i in range(len(cipher_grille)):
        for y in range(len(cipher_grille[i])):
            if cipher_grille[i][y] == "X":
                tmp.append((i, y))
    return ""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
