#
# q = ({"a", "b"}, {"c", "d"})
#
# a = {"a", "b"}
# b = {"v", "a"}
#
# q = a.update(b)
# print(a)
#
# print(a == b)
#
# exit()


class Friends:
    def __init__(self, connections):
        self.connections = connections

    def add(self, connection):
        if connection in self.connections:
            return False
        tmp = list(self.connections)
        tmp.append(connection)
        self.connections = tuple(tmp)
        return True

    def remove(self, connection):
        if connection in self.connections:
            tmp = list(self.connections)
            tmp.remove(connection)
            self.connections = tuple(tmp)
            return True
        return False

    def names(self):
        name = set()
        for con in self.connections:
            name.update(con)
        return name

    # def connected(self, name):
    #     tmp = set()
    #     for connection in self.connections:
    #         if name in connection:
    #             for friend in connection:
    #                 if name != friend:
    #                     tmp.update(friend)
    #     return tmp
    #
    #
    #
    #     return set(
    #         friend
    #         for connection in self.connections if name in connection
    #         for friend in connection if name != friend
    #     )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])

    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    print(letter_friends.connections)
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"