""" Quick demo of weave.inline and comparing the speed of weave to pure python 
and numpy.
"""
from scipy import weave
from numpy import arange

a = arange(10000.)

def weave_sum(a):
    code = """
    double sum = 0.0;
    for (int  i=0 ; i<Na[0]; i++)
	       sum += a[i];
    return_val = sum;
    """
    
    return weave.inline(code, ['a'], compiler="gcc")

def np_sum(a):
    return a.sum()
    
def manual_sum(a):
    total = 0.0
    for elem in a:
        total += elem
    return total