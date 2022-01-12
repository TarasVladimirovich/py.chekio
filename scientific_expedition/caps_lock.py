"""Taras project"""
import re


def caps_lock(text: str) -> str:
    # a_inputs = [m.start() for m in re.finditer('a', text)]
    # result = text.replace('a', '')
    # new_order = [i[1] - i[0] for i in enumerate(a_inputs)]
    #
    # for i in range(0, len(new_order), 2):
    #     if i+1 == len(new_order):
    #         chunk = result[new_order[i]:]
    #     else:
    #         chunk = result[new_order[i]:new_order[i+1]]
    #     result = result.replace(chunk, chunk.upper())

    return ''.join(c.upper() if i % 2 else c for i, c in enumerate(text.split('a')))


if __name__ == "__main__":
    # print("Example:")
    print(caps_lock("Why are you asking me that?"))  # "Why RE YOU sking me thT?"

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
