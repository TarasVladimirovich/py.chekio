from functools import lru_cache
from timeit import timeit

"""This is a recursive function
to find the fibonacci of an integer"""


def fib_recursive(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache()
def fib_recursive_cahced(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


print('Recursive =', [fib_recursive(i) for i in range(7)])
print('Recursive =', [fib_recursive_cahced(i) for i in range(7)])
print(timeit('fib_recursive(30)', globals=globals(), number=10))
print(timeit('fib_recursive_cahced(30)', globals=globals(), number=10))
