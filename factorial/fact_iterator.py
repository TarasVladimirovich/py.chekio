import math
from timeit import timeit

"""This is a iterator function
to find the factorial of an integer"""


class Fact:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.FactIterator(self.n)

    class FactIterator:
        def __init__(self, n):
            self.n = n
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.n:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result


f = Fact(10)
for n, i in enumerate(f):
    print(f'fact of {n}={i}', end='; ')
print()
for n, i in enumerate(f):
    print(f'Fact of {n}={i}', end='; ')
print()
print(timeit('list(Fact(30))', globals=globals(), number=10))
