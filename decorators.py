from datetime import datetime


def spend_time(arg):
    print(arg)
    def outer(func):

        def wrapped(n):
            start = datetime.now()
            result = func(n)
            print(datetime.now() - start)
            return result
        return wrapped

    return outer


@spend_time('one')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@spend_time('two')
def two(n):
    return [x for x in range(n) if x % 2 == 0]


l1 = one(10**7)
l2 = two(10**7)

# print(l1)
# print(l2)