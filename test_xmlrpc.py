""" XMLRPC server with a handler
"""

from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler, \
                               SimpleXMLRPCServer
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
# Override the _dispatch() handler to call the requested function.
class my_handler(SimpleXMLRPCRequestHandler):
    def _dispatch(self, method, params):
        print "CALL", method, params
        return apply(eval(method), params)
    
# Start a server listening for requests on port 8001.
if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 8001), my_handler)
    server.serve_forever()
