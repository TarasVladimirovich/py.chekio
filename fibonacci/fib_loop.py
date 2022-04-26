from timeit import timeit

"""This is a loop function
to find the fibonacci of an integer"""


def fib_loop(n):
    fib_0, fib_1 = 1, 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


print('Loop =', [fib_loop(i) for i in range(10)])
print(timeit('fib_loop(5000)', globals=globals(), number=10))
