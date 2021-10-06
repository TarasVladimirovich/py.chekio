def fact(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr = pr * i
        a.append(pr)
    return a


def fact1(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


print(fact(10))
s = fact1(10)
print(next(s))
print(next(s))
print(next(s))
print(next(s))