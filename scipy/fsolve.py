""" Testing fsolve
"""
from numpy import cos, exp, sin, pi
from scipy.optimize import fsolve


def equations(x,a,b,c):
    x0, x1, x2 = x
    eqs = \
    [3 * x0 - cos(x1*x2) + a,
    x0**2 - 81*(x1+0.1)**2 + sin(x2) + b,
    exp(-x0*x1) + 20*x2 + c]
    return eqs

a = -0.5
b = 1.06
c = (10 * pi - 3.0) / 3
# Optimization start location.
initial_guess = [0.1, 0.1, -0.1]
# Solve the system of non-linear equations.
root = fsolve(equations, initial_guess, args=(a, b, c))
print equations(root, a, b, c)