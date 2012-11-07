""" Simplest possible example of a context manager 
"""

class MyContext(object):
    def __enter__(self):
        print "I entered"
        return self
        
    def __exit__(self, type, value, tb):
        print "Before exiting important things to do..."
        print("Information about potential exception: \n"
              "type=%s, value=%s, trace=%s" % (type, value, tb))
 
if __name__ == "__main__":
    with MyContext() as c:
        print "I am doing things"
        raise RuntimeError("Something bad happened")
        
    print "Continuing normal execution"