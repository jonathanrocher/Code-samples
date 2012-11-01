from SimpleXMLRPCServer import SimpleXMLRPCServer

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

# Start a server listening for requests on port 8001.
if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 8000))
    # Register fact as a function provided by the server.
    server.register_function(fact)
    print "Serving the factorial function on localhost:8000..."
    server.serve_forever()
