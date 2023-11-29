def forward(func, x, h):
    return (func(x + h) - func(x)) / h

def backward(func, x, h):
    return (func(x) - func(x - h)) / h


def centered(func, x, h):
    return (func(x + h) - func(x - h)) / (2 * h)


def richardson(func, x, h):
    return (4 / 3) * centered(func, x, h / 2) - (1 / 3) * centered(func, x, h)
