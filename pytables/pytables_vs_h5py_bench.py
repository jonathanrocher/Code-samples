"""
HDF5 package benchmarking
"""
import tables as tb
import h5py
import numpy as np
import timeit

############################ PYTABLES ################################

def write_file_pytables(a, filename):
    f = tb.openFile(filename, "w")
    group = f.createGroup('/',"random_array_group")
    f.createArray(group, "array", a, "this is a random array")
    f.close()
    return
    
def write_value_array_pytables(filename):
    f = tb.openFile(filename, "r+")
    x = f.root.random_array_group.array
    x[400:600,800] = 0
    f.close()
    return

def load_array_pytables(filename):
    f = tb.openFile(filename, "r")
    x = f.root.random_array_group.array
    result = x[:]
    f.close()
    return result
     
def load_slice_array_pytables(filename):
    f = tb.openFile(filename, "r")
    x = f.root.random_array_group.array
    result = x[500:600,400:800]
    f.close()
    return result
    
def load_value_array_pytables(filename):
    f = tb.openFile(filename, "r")
    x = f.root.random_array_group.array
    result = x[600,800]
    f.close()
    return result

############################ H5PY ####################################

def write_file_h5py(filename, a):
    f = h5py.File(filename, "w")
    subgroup = f.create_group("SubGroup")
    dset = subgroup.create_dataset('MyDataset', data=a)
    f.close()
    return
    
def write_value_array_h5py(filename):
    f = h5py.File(filename, "r+")
    x = f["SubGroup"]["MyDataset"]
    x[400:600,800] = 0
    f.close()
    return

def load_array_h5py(filename):
    f = h5py.File(filename, "r")
    x = f["SubGroup"]["MyDataset"]
    result = x[:]
    f.close()
    return result
     
def load_slice_array_h5py(filename):
    f = h5py.File(filename, "r")
    x = f["SubGroup"]["MyDataset"]
    result = x[500:600,400:800]
    f.close()
    return result
    
def load_value_array_h5py(filename):
    f = h5py.File(filename, "r")
    x = f["SubGroup"]["MyDataset"]
    result = x[600,800]
    f.close()
    return result

    
############################ COMPRESSION ####################################

def write_file_comp_h5py(a, filename=None, lib="gzip", comp=None):
    if filename is None:
        filename = ("random_array_%s%s_h5py.h5" % (lib,comp))
    
    f = h5py.File(filename, "w")
    subgroup = f.create_group("SubGroup")
    ds = subgroup.create_dataset('ds', data = a,
                                 compression=lib, compression_opts=comp)
    f.close()
    return
    
def write_file_comp_pytables(a, filename = None, lib = "blosc", comp = 9):
    if filename is None:
        filename = "random_array_%s%s.h5" % (lib,comp)
    f = tb.openFile(filename, "w")
    group = f.createGroup('/',"random_array_group")
    arr_type = np.dtype("f8")
    atom = tb.Atom.from_dtype(arr_type)
    filters = tb.Filters(complib='blosc', complevel=comp)
    x = f.createCArray(group,"array", atom = atom, shape = (N,N), 
                       filters = filters)
    x[:] = a # Possible to do this by chunk to support unlimited sized a
    f.close()
    return    

if __name__ == "__main__":
    print "pytables version:", tb.__version__
    print "h5py version:", h5py.version.version
    
    N=10**3
#    a = np.random.randn(N,N) 
    b = np.arange(1000)
    b = b[:,np.newaxis]
    c = np.arange(1000)
    c = c[np.newaxis,:]
    a = b+c
    a = a+0.1 

    filename = "random_array.h5"
    """point1 = timeit.default_timer()
    write_file_pytables(a, filename)
    point2 = timeit.default_timer()
    write_value_array_pytables(filename)
    point3 = timeit.default_timer()
    load_array_pytables(filename)
    point4 = timeit.default_timer()
    load_slice_array_pytables(filename)
    point5 = timeit.default_timer()
    load_value_array_pytables(filename)
    point6 = timeit.default_timer()

    filename = "random_array.h5"
"""
    filename = "random_array.h5" 
    write_file_pytables(a, filename) 
    start = timeit.default_timer()
    write_value_array_pytables(filename)
    end = timeit.default_timer()
    print "time writing a value (pytables):", end-start    
    
    filename = "random_array.h5"
    write_file_h5py(filename, a)
    start = timeit.default_timer()
    write_value_array_h5py(filename)
    end = timeit.default_timer()
    print "time writing a value (h5py):", end-start    
    
#####################
# TIMING COMPRESSION
#####################
    start = timeit.default_timer()
    a.tofile("random_array.bin")
    end = timeit.default_timer()
    print "time without compression:", end-start    
 
    start = timeit.default_timer()    
    write_file_comp_pytables(a)
    end = timeit.default_timer()
    print "time with Pytables blosc9:", end-start

    start = timeit.default_timer()
    write_file_comp_h5py(a, lib="gzip", comp=9)
    end = timeit.default_timer()
    print "time with h5py gzip9:", end-start
    
    point1 = timeit.default_timer()
    write_file_comp_h5py(a, lib="lzf")
    point2 = timeit.default_timer()
    print "time with h5py lzf:", point2-point1