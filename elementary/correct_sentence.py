def correct_sentence(text: str) -> str:
    if not text[0].isupper():
        text = text[0].upper() + text[1:]
    if not text[-1] == ".":
        text += "."
    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("welcome to New York"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."