""" Supporting function for memory profiler testing
"""

from numpy import array, int64, float32

def my_func2(b):
    a = 1.0 # Negligible footprint on the memory usage
    c = array(b, dtype = int64)
    c += a
    c = c.astype(float32)
    return c