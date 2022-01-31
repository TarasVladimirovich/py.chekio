import time


def benchmark(func):

    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(f'func name:{func.__name__} \n'
              f'time: {(time.time() - t) * 1000}')
        return res

    return wrapper


@benchmark
def q(n):
    print('hello world')


@benchmark
def qq(n):
    print('hello world')


q(10)
qq(10)
