# import re
#
# VOWELS = "AEIOUY"
# CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
# word = "takot"
#
# flag = True
#
# for i in range(1, len(word)):
#     if (word[i].upper() in VOWELS) == (word[i - 1].upper() in VOWELS):
#         print(i)
#         print(f"{word[i]} {word[i-1]}")
#         # print("first")
#         flag = False
#     if (word[i].upper() in CONSONANTS) == (word[i - 1].upper() in CONSONANTS):
#         # print("secong")
#         flag = False
#
# print(flag)
# exit()
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    lst = re.findall(r"[\w']+", text)
    for word in lst:
        flag = True
        if len(word) == 1 or word.isdigit():
            continue
        if True in list(map(lambda x: x.isdigit(), word)):
            continue
        for i in range(1, len(word)):
            if (word[i].upper() in VOWELS) == (word[i-1].upper() in VOWELS):
                flag = False
        if flag:
            count += 1
    return count


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"