def fibonacci_sum_squares(n):
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

    period = pisano_period(10)
    n_mod_period = n % period

    fn = fibonacci_modulo(n_mod_period, 10)
    fn1 = fibonacci_modulo((n_mod_period + 1) % period, 10)

    return (fn * fn1) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
