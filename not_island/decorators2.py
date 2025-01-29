from datetime import datetime


def timer(name):
    def outer(func):
        def wrapped(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(f"{func.__name__} {name}: {datetime.now() - start}")
            return result

        return wrapped

    return outer


@timer("one")
def loop(value):
    l = []
    for i in range(value):
        if i % 2 == 0:
            l.append(i)
    return l


@timer("two")
def list_compr(value):
    return [x for x in range(value) if x % 2 == 0]


@timer("three")
def generator_(value):
    return (x for x in range(value) if x % 2 == 0)


@timer("four")
def filt(value):
    return filter(lambda x: x % 2 == 0, range(value))


l1 = loop(10 ** 8)
l2 = list_compr(10 ** 8)
l3 = generator_(10 ** 8)
l4 = filt(10 ** 8)
