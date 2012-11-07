""" File to test the memory profiler package. To run it, 

python -m memory_profiler mem_profile_test.py 
"""

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()