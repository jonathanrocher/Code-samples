""" Before this code is run in a given session, an ipython cluster session needs 
to be started. This can be done with 4 engines using the ipcluter command:

    $ ipcluster start -n 4
    
More engines can be added on the fly by starting another 1
    
    $ ipengine
"""
from IPython.parallel import Client
import time

# This assumes that the client will connect to the default profile. If not, a 
# profile or a json file can be provided to the client at creation.
c = Client() 
print "The client contains 4 different engines with different IDs", c.ids

# 2 different kinds of view on the engines:
direct_view_engine_0 = c[0]
load_balanced_view = c.load_balanced_view()

# Let's define what we want our engines to do for us
mul = lambda x,y: x*y
direct_view_engine_0.apply(mul, 4, 5)

# The loadbalanced view can receive a map_sync or map_async with a callable and 
# a list of arguments.
load_balanced_view.map_sync(mul, range(5), range(10, 15))

# c[:] is a (multiplexer) direct view on all 4 engines. It can apply a target 
# function to all engines. This version is asynchronous: the result will be 
# stored separately for each engine.
c[:].apply_async(mul, 4, 5).get_dict()


def test_latency(view, nb_tasks):
    """ Measure the latency of a given direct view on an engine for a given 
    setup where nb_tasks tasks are sent to it.
    """
    tic = time.time()
    echo = lambda x: x
    tic = time.time()
    for i in xrange(nb_tasks):
        view.apply_async(echo, '')
    toc = time.time()
    view.wait()
    tac = time.time()
    sent = toc-tic
    roundtrip = tac-tic
    return sent, roundtrip
    
# test overhead related to 
for client in c:
    print 