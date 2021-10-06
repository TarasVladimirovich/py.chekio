from datetime import datetime


def spend_time(arg):
    def outer(func):
        def wrapped(n):
            start = datetime.now()
            result = func(n)
            print(f'{func.__name__}: {datetime.now() - start}')
            return result

        return wrapped

    return outer


@spend_time('one')
def one(value):
    l = []
    for i in range(value):
        if i % 2 == 0:
            l.append(i)
    return l


@spend_time('two')
def two(value):
    return [x for x in range(value) if x % 2 == 0]


@spend_time('three')
def three(value):
    return list(filter(lambda x: x % 2 == 0, range(value)))


l1 = one(10 ** 8)
l2 = two(10 ** 8)
l3 = three(10 ** 8)

# print(l1)
# print(l2)
