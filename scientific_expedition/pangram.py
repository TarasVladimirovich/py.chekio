def check_pangram(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print(set(alphabet).issubset(text.lower()))
    return set(alphabet).issubset(text.lower())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    check_pangram("The quick brown fox jumps over the lazy dog.")
    # assert not check_pangram("ABCDEF"), "ABC"
    # assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    # print('If it is done - it is Done. Go Check is NOW!')
