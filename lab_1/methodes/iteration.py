from methodes.open_txt import *


def calc_itaration(n):
    a, b = -5.0, 5.0
    k = 0.0
    x0 = (a + b) / 2.0
    accuracy = 1e-3
    while True:
        xk = f(n, x0)
        if (abs(xk - x0) < accuracy):
            break
        else:
            x0 = xk
        if abs(a - x0) > accuracy and abs(b - x0) > accuracy:
            return xk
