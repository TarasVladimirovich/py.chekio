import re


def from_camel_case(name: str) -> str:
    print('_'.join(re.findall('([A-Z][^A-Z]*)', name)).lower())
    result = ""
    for i in name:
        if i.isupper():
            result += "_"
            result += i.lower()
        else:
            result += i
    return result[1:]


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("MyFunctionName"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
