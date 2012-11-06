""" Basic XMLRPC clien/server: client side.

To illustrate the power of this technology, start 2 python sessions, and start 
the server in one and run the client code on the other.
"""
# Simplest version of accessing the server
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
print "3 is even: %s" % proxy.is_even(3)
print "100 is even: %s" % proxy.is_even(100)


# Multicall access:
multicall = xmlrpclib.MultiCall(proxy)
for i in range(10):
    multicall.is_even(i)

result = multicall()

print tuple(result)