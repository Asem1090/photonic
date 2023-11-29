from abc import ABC, abstractmethod
from math import sqrt
from typing import Iterable


class Distribution(ABC):

    def __init__(self):
        self.values = []

    @abstractmethod
    def cumulative_distribution_function(self, x):
        ...

    @abstractmethod
    def next(self, number=1) -> float:
        ...

    @abstractmethod
    def get_expected_mean(self) -> float:
        ...

    @abstractmethod
    def get_expected_variance(self) -> float:
        ...

    def get_expected_standard_deviation(self) -> float:
        return sqrt(self.get_expected_variance())

    def get_mean(self) -> float:
        return sum(self.values) / len(self.values)

    def get_variance(self) -> float:
        mean = self.get_mean()
        return sum([(value - mean) ^ 2 for value in self.values]) / len(self.values)

    def get_standard_deviation(self) -> float:
        return sqrt(self.get_variance())


class Poisson(Distribution):

    def __init__(self, rate):
        super().__init__()
        self.rate = rate

    def CDF(self, x):
        ...

    def next(self, number=1) -> float:
        ...

    def get_expected_mean(self) -> float:
        return self.rate

    def get_expected_variance(self) -> float:
        return self.rate


def integral(x: Iterable, y: Iterable):
    if len(x) != len(y):
        raise ValueError("X length must be the same as Y length")
    elif len(x) % 3 != 1:
        raise ValueError("X length must be a multiple of 3 plus 1")
    elif len(x) < 4:
        raise ValueError("X length must be 4 or more")
    else:
        h = x[1] - x[0]
        for i in range(1, len(x)-1):
            if (x[i+1]-x[i]) != h:
                raise ValueError("This function only accepts X's with equal distance between them")

    return 3*h/8 * (y[0] + y[-1] + 3*sum(y[1::3]) + 3*sum(y[2::3]) + 2*sum)


class Gamma(Distribution):

    def __init__(self, shape_factor, rate):
        super().__init__()
        self.shape_factor = shape_factor
        self.rate = rate

    def gamma(self, r):
        # x = 1/t; t = 1/x;

        # divide the integral into 0 to 1 f(x)dx and f(t)dt from 1/1 to 1/infinity = 1 to 0
        # Then we make it negative and it becomes from 0 to 1
        xarr = (xi for xi in range(0, 1, 1E-1_000_000))
        tarr = (ti for ti in range(0, 1))
        integral()

    def next(self, number=1) -> float:
        ...

    def get_expected_mean(self) -> float:
        return self.shape_factor / self.rate

    def get_expected_variance(self) -> float:
        return self.shape_factor / self.rate ^ 2
