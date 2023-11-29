def trapz(func, start, end, intervals=1000):
    if start > end:
        return -1 * trapz(func, start, end, intervals)

    if intervals < 1 or type(intervals) != int:
        raise ValueError("Intervals must be positive int")

    h = (end - start) / intervals
    x = (i for i in range(start, end+h, h))
    y = [func(i) for i in x]

    return h/2 * (y[0] + y[-1] + 2*sum(y[1:-1]))


def simpsons_three_eighths(func, start, end, intervals=1000):
    if start > end:
        return -1 * simpsons_three_eighths(func, start, end, intervals)

    if intervals < 1 or type(intervals) != int:
        raise ValueError("Intervals must be positive int")

    while intervals % 3 != 0:
        intervals += 1

    h = (end - start) / intervals
    x = (i for i in range(start, end+h, h))
    y = [func(i) for i in x]

    return 3*h/8 * (y[0] + y[-1] + 3*sum(y[1:-2:3]) + 3*sum(y[2:-1:3]) + 2*sum(y[3:-3:3]))
