""" Basic XMLRPC clien/server: server side 

To illustrate the power of this technology, start 2 python sessions, and start 
the server in one and run the client code on the other.
"""

###############################################################################
# Required code
###############################################################################

from SimpleXMLRPCServer import SimpleXMLRPCServer

def is_even(n):
    return n%2 == 0


server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(is_even, "is_even")

###############################################################################
# Optional code to illustrate passing more complex objects
###############################################################################
import datetime
import xmlrpclib

def today():
    today = datetime.datetime.today()
    return xmlrpclib.DateTime(today)

server.register_function(today, "today")

###############################################################################
# Optional code to illustrate supporting mutliple calls in one HTTP request
# See the client code to see what this allows.
###############################################################################

server.register_multicall_functions()

###############################################################################
# Required code
###############################################################################

server.serve_forever()

