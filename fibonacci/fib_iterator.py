class FibIter:

    def __init__(self, n):
        self.n = n
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self.n:
            raise StopIteration
        else:
            result = self.fib(self._i)
            self._i += 1
            return result

    def fib(self, n):
        fib_0, fib_1 = 1, 1
        for i in range(n - 1):
            fib_0, fib_1 = fib_1, fib_0 + fib_1
        return fib_1


f = FibIter(10)
for n, i in enumerate(f):
    print(f'Fib of {n}={i}')
