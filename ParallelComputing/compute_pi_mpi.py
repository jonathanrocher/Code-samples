# -*- coding: utf-8 -*-
from mpi4py import MPI
import math

def compute_pi(n, start=0, step=1):
    """ Pure python integration of 4/(1+x**2) which gives pi
    """
    h = 1.0 / n
    s = 0.0
    for i in range(start, n, step):
        x = h * (i + 0.5)
        s += 4.0 / (1.0 + x**2)
    return s * h
    
comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

if myrank == 0:
    n = 10
else:
    n = None
    
n = comm.bcast(n, root=0)

mypi = compute_pi(n, myrank, nprocs)

pi = comm.reduce(mypi, op=MPI.SUM, root=0)

if myrank == 0:
    error = abs(pi - math.pi)
    print ("pi is approximately %.16f, "
           "error is %.16f" % (pi, error))