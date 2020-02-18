class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    def attack_opponent(self, other_warrior):
        other_warrior.take_hit(self)
        return other_warrior.is_alive

    def take_hit(self, other_warrior):
        self.health -= other_warrior.attack
        return True

    @property
    def is_alive(self) -> bool:
        return self.health > 0


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attack_opponent(unit_2)
        if not unit_2.is_alive:
            return unit_1.is_alive
        unit_2.attack_opponent(unit_1)
    return unit_1.is_alive


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False