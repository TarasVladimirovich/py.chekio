VOWELS = "aeiouy"
CONSONANT = 'bcdfghjklmnpqrstvwxz'

# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);


def rule1(word):
    new_word = list(word)
    count = 0
    for chr in new_word:
        if chr in CONSONANT:
            new_word.pop(count+1)
        elif chr in VOWELS:
            new_word.pop(count+1)
            new_word.pop(count+1)
        count += 1
    return "".join(new_word)


def translate(phrase):
    word = rule1(phrase)
    return word


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))


    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")