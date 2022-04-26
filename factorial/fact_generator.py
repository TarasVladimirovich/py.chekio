from timeit import timeit

"""This is a generator function
to find the factorial of an integer"""


def fact_generator(n):
    result = 1
    for i in range(1, n + 1):
        yield result
        result *= i


f = fact_generator(10)
for n, i in enumerate(f):
    print(f'Fib of {n}={i}')
print(timeit('fact_generator(5000)', globals=globals(), number=10))
