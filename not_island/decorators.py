# decorator which prints invocation
def verbose(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        print("{}: *args: {}, **kwargs: {}".format(name, args, kwargs))
        result = func(*args, **kwargs)
        print("{}: return: {}".format(name, result))
        return result
    return wrapper


# decoreate a fuction at runtime
sum((1, 2, 4))
verbose_sum = verbose(sum)
verbose_sum((1, 2, 4))

# decorate a lambda at runtime
compare = verbose(lambda a, b: f'Are objects equal? : {a == b}')
compare('s', 'sv')

# decorate a function at definition time
@verbose
def concatenate(*values):
    return "".join(map(str, values))


concatenate(1, "3ddd", 3.4)