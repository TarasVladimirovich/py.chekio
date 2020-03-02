

# s = "1.2"
# print(float(s))
# exit()
import copy


def fastest_horse(horses: list) -> int:
    # new_tmp = list(list(range(len(horses))) for _ in range(len(horses[0])))
    # for i in range(len(horses)):
    #     for y in range(len(horses[i])):
    #         number = float(horses[i][y].replace(":", "."))
    #         new_tmp[y][i] = number
    # minimum = sum(new_tmp[0])
    # index = 0
    # count = 0
    # for i in new_tmp:
    #     if sum(i) < minimum:
    #         minimum = sum(i)
    #         index = count
    #     count += 1
    # return index+1
    # r is all candidate
    r = range(len(horses[0]))
    print(r)
    # At first, we make winner list.
    winner_list = [min(r, key=race.__getitem__) for race in horses]
    for race in horses:
        print(race.__getitem__)
    print(winner_list)
    # Second, we determine maximum winner.
    m = max(r, key=winner_list.count) + 1
    print(m)
    return ""


if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([["1:55","1:50","1:45","1:40","1:35"],
                         ["2:55","2:50","2:45","2:40","2:35"],
                         ["3:55","3:50","3:45","3:40","3:35"],
                         ["4:55","4:50","4:45","4:40","4:35"],
                         ["3:55","3:50","3:45","3:40","3:35"],
                         ["2:35","2:40","2:45","2:50","2:55"],
                         ]))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")