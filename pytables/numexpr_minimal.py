import numpy as np
import numexpr as ne

a = np.arange(10)
b = np.arange(10)
c = ne.evaluate("2*a+b")
print c
d = ne.evaluate("sum(a, axis=0)")
print d
e = ne.evaluate("log(a)")
print e

