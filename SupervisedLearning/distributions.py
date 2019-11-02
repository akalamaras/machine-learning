"""
    Author: Alexandros Kalamaras
    Date: 02 November 2019
"""

import numpy as np


def integrate(func, a, b, N):
    """
    Integrates a function

    :param func: A function that takes 1 argument e.g. sin
    :param a: The beginning of the line
    :param b: The end of the line
    :param N: The number of points between a and b
    :return: The area after integration
    """
    x = np.linspace(a, b, N)
    fx = func(x)
    area = np.sum(fx) * (b - a) / N
    return area


def compute_mean(func, a, b, N):
    """
    Computes the mean after integrating a function

    :param func: A function that takes 1 argument e.g. sin
    :param a: The beginning of the line
    :param b: The end of the line
    :param N: The number of points between a and b
    :return: The mean after integration
    """
    def xfx(x):
        return np.multiply(x, func(x))

    mean = integrate(xfx, a, b, N)
    return mean


def compute_variance(func, a, b, N):
    """
    Computes the variance after integrating a function

    :param func: A function that takes 1 argument e.g. sin
    :param a: The beginning of the line
    :param b: The end of the line
    :param N: The number of points between a and b
    :return: The variance after integration
    """

    def xfx(x):
        return np.multiply(x, func(x))

    def xxfx(x):
        return np.multiply(x*x, func(x))

    mean = integrate(xfx, a, b, N)
    variance = integrate(xxfx, a, b, N) - (mean * mean)
    return variance
