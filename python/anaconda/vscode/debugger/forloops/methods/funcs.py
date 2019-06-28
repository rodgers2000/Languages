def func1(y):
    return y + 10


def func2(z):
    return z + 20


def func3(x):
    return func2(func1(x))  # add 30
