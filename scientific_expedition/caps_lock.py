import re


def caps_lock(text: str) -> str:
    q = [m.start() for m in re.finditer('a', text)]
    result = ''
    for i in q:
        result = text.replace(text[i], '')
    for i in range(0, len(q), 2):
        if i+1 == len(q):
            result = text.replace(text[q[i]+1:], text[q[i]+1:].upper())
        else:
            result = text.replace(text[q[i]:q[i+1]], text[q[i]:q[i+1]].upper())
            print()

    # print(result.replace('a', ''))
    result = result.replace('a', '')
    print(result)
    return result


if __name__ == "__main__":
    # print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    # assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    # assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
