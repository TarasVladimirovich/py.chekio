from functools import lru_cache
from timeit import timeit

"""This is a recursive function
to find the factorial of an integer"""


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


@lru_cache()
def factorial_cached(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print('Recursive =', [factorial(i) for i in range(1, 20)])
print('Recursive =', [factorial_cached(i) for i in range(1, 20)])
print(timeit('factorial(20)', globals=globals(), number=10))
print(timeit('factorial_cached(20)', globals=globals(), number=10))
