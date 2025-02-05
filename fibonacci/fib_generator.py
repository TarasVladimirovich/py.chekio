from timeit import timeit

"""This is a generator function
to find the fibonacci of an integer"""


def fib_gen(n):
    fib_0, fib_1 = 1, 1 # fib_0, fib_1 = 0, 1
    yield fib_0
    yield fib_1
    for i in range(n - 2): # (n -1)
        print(i)
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


f = list(fib_gen(3))
print(f[-1])
for n, i in enumerate(f):
    print(f'Fib of {n}={i}')
# print(timeit('list(fib_gen(5000))', globals=globals(), number=1))
