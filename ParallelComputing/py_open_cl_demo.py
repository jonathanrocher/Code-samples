""" Demo of PyOpenCL that multiply a numpy array by 2
"""

import pyopencl as cl
import numpy

# Create some 1D data
a = numpy.random.rand(256**3).astype("float32")

# Create a GPU context to contain that data and a queue to receive commands
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# Allocate a chunk of memory of the size of a and copy the data
a_dev = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, size = a.nbytes)
cl.enqueue_write_buffer(queue, a_dev, a)

# create the pyopencl function a little like weave.inline
# Just in Time compiler. 
# Notice the way we index into the array a: get_global_id collect the worker's 
# ID for each worker and use it as index into the array: this is how parallelism 
# is achieved. 
prg = cl.Program(ctx, """
    __kernel void twice(__global float *a)
    {
        unsigned int i = get_global_id(0);
        a[i] *= 2;
    }""").build()
    
# Call the twice function    
prg.twice(queue, a.shape, (1,), a_dev)

# Retrieve result
result = numpy.empty_like(a)
cl.enqueue_read_buffer(queue, a_dev, result).wait()
print "Succes?", numpy.all(result-2*a == 0.)