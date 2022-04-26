from timeit import timeit

"""This is a generator function
to find the fibonacci of an integer"""


def fib_gen(n):
    fib_0, fib_1 = 1, 1
    yield fib_0
    yield fib_1
    for i in range(n - 2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


f = fib_gen(10)
for n, i in enumerate(f):
    print(f'Fib of {n}={i}')
print(timeit('list(fib_gen(5000))', globals=globals(), number=1))
