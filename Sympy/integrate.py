""" Analytical computations with sympy
"""
import sympy
from sympy.abc import a,b,c

y = 2*a+b**c
print "Integral of y with respect to a:"
print sympy.integrate(y, a)
