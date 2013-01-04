""" Demo file for testing memory profiling with memory_profiler and heapy. 

"""
# Line below is necessary to run the code without -m memory_profiler
from memory_profiler import profile
from memory_profiler_support import my_func2

    
@profile
def my_func():
    result = {}
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    c = my_func2(b)
    del b
    result["a"] = a
    result["c"] = c
    return result

class MyClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = linspace(self.y)

if __name__ == '__main__':
    a = my_func()
    
    try:
        from guppy import hpy
        hp = hpy()
        h1 = hp.heap()
        print h1
        print h1.bymodule
    except ImportError:
        print "heapy is not installed on your machine"