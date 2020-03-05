

def recall_password(cipher_grille, ciphered_password):
    tmp = []
    rot_mat = [list(x) for x in cipher_grille]

    def add_point(matrix):
        for i in range(len(matrix)):
            for y in range(len(matrix[i])):
                if matrix[i][y] == "X":
                    tmp.append((i, y))

    def rotate90Clockwise(A):
        N = len(A[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                A[j][N - 1 - i] = temp

    for i in range(4):
        add_point(rot_mat)
        rotate90Clockwise(rot_mat)
    result = ""
    for i in tmp:
        result += ciphered_password[i[0]][i[1]]
    return result


if __name__ == '__main__':

    recall_password(('X...',
                    '..X.',
                    'X..X',
                    '....'),
                    ('itdf',
                     'gdce',
                     'aton',
                     'qrdi'))

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
