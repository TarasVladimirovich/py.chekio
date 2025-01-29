from collections import Counter

def most_frequent(data: list) -> str:
    d = {x: data.count(x) for x in set(data)}
    return sorted(d, key=d.get, reverse=True)[0]

def most_frequent(data: list) -> str:
    tmp = Counter(data)
    return sorted(tmp, key=tmp.get, reverse=True)[0]

def most_frequent(data: list) -> str:
    final = {}
    for i in data:
        final[i] = final.get(i, 0) + 1
    return sorted(final, key=final.get, reverse=True)[0]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    assert most_frequent([1, 2, 3, 4, 5, 6, 7, 88, 1, 1, 1, 2, 3, 2, 2, 3, 34]) == 1
    print("Done")
#
# print(["a", "b", "c", "a", "b", "a"].count("a"))
# print(Counter[["a", "b", "c", "a", "b", "a"]])
# print(Counter(["a", "b", "c", "a", "b", "a"]))
# print(Counter([1, 2, 3, 4, 5, 6, 7, 88, 1, 1, 1, 2, 3, 2, 2, 3, 34]))