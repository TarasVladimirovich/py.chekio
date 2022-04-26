from timeit import timeit

"""This is a loop function
to find the factorial of an integer"""


def fact_loop(x):
    res_ = 1
    for i in range(1, x+1):
        res_ *= i
    return res_


print('Loop =', [fact_loop(i) for i in range(1, 10)])
print(timeit('fact_loop(5000)', globals=globals(), number=10))
