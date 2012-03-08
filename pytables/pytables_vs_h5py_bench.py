"""
HDF5 package benchmarking
"""
import tables as tb
import h5py
import numpy as np

############################ PYTABLES ################################

def write_file_pytables(filename, a):
    f = tb.openFile(filename, "w")
    group = f.createGroup('/',"random_array_group")
    f.createArray(group, "array", a, "this is a random array")
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
    
if __name__ == "__main__":
    print "pytables version:", tb.__version__
    print "h5py version:", h5py.version.version
    
    N=10**4
    a = np.random.randn(N,N)    

    filename="random_array.h5"
    # Actual benchmarking left to be done in ipython with %timeit

