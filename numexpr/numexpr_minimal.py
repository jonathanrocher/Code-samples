""" Getting started with numexpression 
"""

import numpy as np
from numexpr import evaluate

N = 8
a = np.arange(10**N)
b = np.arange(10**N)
# Numpy version
c1 = 2*a**3+b**2+16
# Numexpr version
c2 = evaluate("2*a**3+b**2+16")

# Exploring the other available operators
a = np.random.random((1000,1000))
d = evaluate("sum(a, axis=0)")
print "The sum of all elements:", d
e = evaluate("log(a)")
print "The log of all elements:", e