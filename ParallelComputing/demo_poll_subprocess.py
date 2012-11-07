""" Demo creating a subprocess and doing something in the master process when 
the child is running. To know about the child's state we demo the poll method of 
the process. 
"""

from subprocess import Popen
import sys
print "Starting..."
# sleep for 10 seconds
p = Popen(['sleep','10'])
# continue on with processing
print "Continuing",
k=0
while p.poll() is None:
  k += 1 
  if (k % 100000) == 0: 
      print k//100000,
      sys.stdout.flush()
print
print "Done", p.returncode
