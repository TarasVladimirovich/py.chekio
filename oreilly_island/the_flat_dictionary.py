def flatten(dictionary):

    def inner(key, dictionary):
        tmp = {}
        for k, v in dictionary.items():
            result = key + k
            if isinstance(v, dict) and len(dictionary[k]) != 0:
                tmp.update(inner(result + '/', dictionary[k]))
            else:
                if len(dictionary[k]) == 0:
                    v = ''
                tmp.update({result: v})
        return tmp
    return inner('', dictionary)


if __name__ == '__main__':
    # test_input = {"key": {"deeper": {"more": {"enough": "value", "second": "value2"}}}}
    # test_input = {"empty": {}}
    test_input = {"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    print('Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
