""" Hello world for running a python script on multiple nodes 
using MPI. Run it with
$ mpiexec -n 4 python hello_world.py
"""

from mpi4py import MPI
import os

print 'Hello, World from %s!' % os.getpid()
