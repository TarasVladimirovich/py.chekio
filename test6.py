a = [i for i in range(1, 10, 2)]
b = [i for i in range(2, 21, 2)]
c = {x: x ** 3 for x in range(1, 10) if x not in [x for x in range(4, 8)]}
# print(a)
# print(b)
# print(c)


def merge(list1, list2):
    maxim = min(len(a), len(b))
    tmp = []
    for i in range(maxim):
        tmp.append(list1[i])
        tmp.append(list2[i])
    if list1 < list2:
        tmp.extend(list2[maxim:])
    else:
        tmp.extend(list1[maxim:])
    print(tmp)


def merge1(list1, list2):
    maxim = max(len(a), len(b))
    tmp = []
    for i in range(maxim):
        if len(list1) > i:
            tmp.append(list1[i])
        if len(list2) > i:
            tmp.append(list2[i])

    print(tmp)


def merge2(list1, list2):
    for i in (list1, list2):
        print(i)

    # print(tmp)


merge2(a, b)