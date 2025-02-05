# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if from_ > to:
        return 0

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
        _sum = 1
        for _ in range(n - 1):
            previous, current = current, (previous + current) % m
            _sum = (_sum + current) % m
        return _sum

    period = pisano_period(10)

    to_sum = fibonacci_modulo_sum(to % period, 10)
    from_sum = fibonacci_modulo_sum((from_ - 1) % period, 10) if from_ > 0 else 0

    result = (to_sum - from_sum) % 10
    return result


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
