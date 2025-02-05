def fibonacci_number(n):
    def inner(n):
        fib_0, fib_1 = 1, 1
        yield fib_0
        yield fib_1
        for i in range(n - 2):
            fib_0, fib_1 = fib_1, fib_0 + fib_1
            yield fib_1

    if n <= 1:
        return n
    else:
        return max((inner(n)))


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

