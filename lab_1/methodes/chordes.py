from methodes.open_txt import *


def calc_chord(n):
    accuracy = 1e-3
    a, b = -1000, 1000
    while abs(b - a) > accuracy:
        a = b - (b - a) * f(n, b) / (f(n, b) - f(n, a))
        b = a - (a - b) * f(n, a) / (f(n, a) - f(n, b))
    return b
