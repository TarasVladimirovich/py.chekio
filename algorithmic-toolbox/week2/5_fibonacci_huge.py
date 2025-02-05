def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    def pisano_period(m):
        previous, current = 0, 1
        for i in range(m * m):
            previous, current = current, (previous + current) % m
            if previous == 0 and current == 1:
                return i + 1

    def fibonacci_modulo(n, m):
        if n <= 1:
            return n
        previous, current = 0, 1
        for _ in range(n - 1):
            previous, current = current, (previous + current) % m
        return current

    period = pisano_period(m)
    n_mod_period = n % period
    return fibonacci_modulo(n_mod_period, m)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
