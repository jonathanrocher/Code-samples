"""
"""

import multiprocessing as mp
import sys
from time import sleep


def process_action(proc_num, n):
    """ Take a child process, print its PID and sleep for n seconds
    """
    proc = mp.current_process()
    proc_name = proc.name
    proc_id = proc.pid
    print "Child process number %s " % proc_num
    sys.stdout.flush()
    sleep(n)
    print "Process %s is done" % proc_num
    sys.stdout.flush()
    
if __name__ == "__main__":
    nb_processes = 10
    for i in range(nb_processes):
        p = mp.Process(target=process_action, args = (i, i+10))
        p.start()
        
    [p.join() for p in mp.active_children()]
    print "Main process can keep running now that they all have joined"
    sys.stdout.flush()