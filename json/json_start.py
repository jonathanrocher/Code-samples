import json

class my_class(object):
    a = 1
    
    #def increase_a(self):
    #    self.a += 1
    #    print "New a is %s" % self.a

def my_class_json_dumphook(z):
    """ Create a hook to be able to serialize my_class type objects
    """
    #return '{"class": "%s", "value": %s}' % (z.__class__, z.a)
    return {"class": str(z.__class__), "value": z.a}

def explore_dumping(x, y, z, var_in_file, filename):
    """
    """
    print json.dumps(x)
    print json.dumps(y)
    try:
        print json.dumps(z)
    except Exception as e:
        print "dumping z as is didn't work: exception is %s" % e
        print "Using the object hook"
        dump = json.dumps(z, default = my_class_json_dumphook)
        print dump


    f = open(filename, "w")
    try:
        json.dump(var_in_file, f, indent=4)
    except TypeError as e:
        json.dump(var_in_file, f, indent=4, default = my_class_json_dumphook)
    f.close()
    return 

def explore_loading(filename):
    
    f = open(filename, "r")
    try:
        print json.load(f)
    except Exception as e:
        print "Error loading the file with exception %s" % e
    f.close()
    return 

if __name__ == "__main__":
    x = {"a": 1, "b": 2, "c": 3}
    y = [1,2,3,4,5,6]
    z = my_class()

    filename = "json_start.cfg"

    explore_dumping(x, y, z, z, filename)
    
    explore_loading(filename)
    
