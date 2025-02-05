def fibonacci_sum(n):
    if n <= 1:
        return n

    def pisano_period(m):
        previous, current = 0, 1
        for i in range(m * m):
            previous, current = current, (previous + current) % m
            if previous == 0 and current == 1:
                return i + 1

    def fibonacci_modulo_sum(n, m):
        if n <= 1:
            return n
        previous, current = 0, 1
        _sum = 1  # Sum of F(0) and F(1)
        for _ in range(n - 1):
            previous, current = current, (previous + current) % m
            _sum = (_sum + current) % m
        return _sum

    period = pisano_period(10)
    n_mod_period = n % period
    return fibonacci_modulo_sum(n_mod_period, 10)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
