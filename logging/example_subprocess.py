import subprocess

cmd = ['ls', '-l']
subproc = subprocess.Popen(cmd, stdout = subprocess.PIPE, 
                           stderr = subprocess.PIPE)
# The call to communicate is a way to force the rest of the execution to wait 
# until the subprocess finished
comm_out, comm_err = subproc.communicate()
print "Output:", comm_out
print "Error msg:", comm_err
