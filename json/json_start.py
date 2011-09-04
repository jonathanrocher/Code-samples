import json

class my_class(object):
    a = 1
    
    def increase_a(self):
        self.a += 1
        print "New a is %s" % self.a

def my_class_json_hook(z):
    """ Create a hook to be able to serialize my_class type objects
    """
    print "z", type(z)
    return '{"class": %s, "value": %s}' % (z.__class__,z.a)

def explore_dumping(x,y,z):
    """
    """
    print json.dumps(x)
    print json.dumps(y)
    try:
        print json.dumps(z)
    except Exception as e:
        print "dumping z as is didn't work: exception is %s" % e
        print "Using the object hook"
        print json.dumps(z, default = my_class_json_hook)
        print eval(json.dumps(z, default = my_class_json_hook))

    f = open("json_start.cfg", "w")
    json.dump(x, f, indent=4)
    f.close()

if __name__ == "__main__":
    x = {"a": 1, "b": 2, "c": 3}
    y = [1,2,3,4,5,6]
    z = my_class()
    
    explore_dumping(x,y,z)
    
