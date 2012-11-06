""" Hello world for running a python script on multiple nodes 
using MPI. Run it with
$ mpiexec -n 4 python hello_world.py
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
myrank = comm.Get_rank()
print 'Hello, World from', myrank
