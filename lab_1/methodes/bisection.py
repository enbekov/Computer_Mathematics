from methodes.open_txt import *


def calc_bisect(line_nubmer):
    accuracy = 1e-3
    a, b = -1000, 1000
    while b - a > accuracy:
        c = (a + b) / 2.0
        if f(line_nubmer, b) * f(line_nubmer, c) < 0:
            a = c
        else:
            b = c
    return (a + b) / 2.0
