from methodes.open_txt import *
from sympy import diff, Symbol, cos, sin


def calc_newton(n, x0):
    accuracy = 1e-3
    list_newton = get_all_equations()
    x = Symbol('x')
    f = eval(list_newton[n])
    f1 = diff(f, x)
    x0 = float(x0)
    while True:
        x1 = x0 - (f.subs(x, x0) / f1.subs(x, x0))
        if abs(x1 - x0) < accuracy:
            return x1
        x0 = x1
