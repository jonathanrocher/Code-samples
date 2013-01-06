""" Comparing execution time between Numexpr and Numpy
"""

import numpy as np
from numexpr import evaluate
import time
from matplotlib.pyplot import (figure, plot, show, legend, xlabel, ylabel, 
                               yscale, title)

exec_times_np = []
exec_times_ne = []

sizes = np.arange(0, 8, 0.5)
for N in sizes:
    a = np.arange(10**N)
    b = np.arange(10**N)
    start1 = time.time()
    c1 = 2*a**3+b**2+16
    start2 = time.time()
    exec_times_np.append(start2-start1)
    print "Numpy polynomial computation %s seconds" % (start2-start1)
    start3 = time.time()
    c2 = evaluate("2*a**3+b**2+16")
    t4 = time.time()
    print "Using numexpr, the polynomial computation took %s seconds" % (t4-start3)
    exec_times_ne.append(t4-start3)
    del a
    del b
    del c1
    del c2

figure()
plot(sizes, exec_times_np, label = "Numpy")
plot(sizes, exec_times_ne, label = "Numexpr")
xlabel("log10(size(arrays))")
ylabel("execution time in sec")
yscale("log")
title("Comparing execution time to compute 2*a**3+b**2+16")
legend(loc="upper left")
show()

