import re


def to_camel_case(name: str) -> str:
    r = re.findall('(_[a-z])', name)
    for i in r:
        name = name.replace(i, i[1].capitalize())
    return name[0].upper() + name[1:]


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('my_function_name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
