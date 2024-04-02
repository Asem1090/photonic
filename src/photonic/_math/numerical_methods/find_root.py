def bisection(func, lower_limit, upper_limit, tolerance):
    if func(lower_limit) * func(upper_limit) > 0:
        raise ValueError("Function must have different signs at the lower and upper limits!")

    return __bisection(func, lower_limit, upper_limit, tolerance)


def __bisection(f, l, u, t):
    mid = (l + u) / 2
    if abs(l - u) < t:
        return mid

    fm = f(mid)

    if fm * f(l) > 0:
        return __bisection(f, mid, u, t)
    else:
        return __bisection(f, l, mid, t)


def secant(func, guess1, guess2, tolerance):
    return __secant(func, guess1, guess2, tolerance)


def __secant(f, current, prev, t):
    fc = f(current)
    fp = f(prev)
    if abs(fc - fp) / fc < t:
        return current
    else:
        return __secant(f, current - (f(current) * (prev - current)) / (f(prev) - f(current)), current, t)
