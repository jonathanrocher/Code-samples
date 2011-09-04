import json

class my_class(object):
    a = 1

    def __init__(self, a = None):
        if a:
            self.a = a

    def increase_a(self):
        self.a += 1
        print "New a is %s" % self.a

def my_class_json_dumphook(z):
    """ Create a hook to be able to serialize my_class type objects
    """
    return {"class": str(z.__class__), "value": z.a}

def my_class_json_loadhook(in_dict):
    """ Create a hook to recreate a my_class type object from the dict given by 
        my_class_json_dumphook.
    """
    if in_dict["class"].find("my_class") != -1:
        return my_class(a = in_dict["value"])

def explore_dumping(x, y, z, var_in_file, filename):
    """ Test dumping the object to a string and a file
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
    """ Test loading a non-standard object from a file
    """
    f = open(filename, "r")
    try:
        new_z = json.load(f, object_hook = my_class_json_loadhook)
        print ("Recreated object is : %s " % new_z)
    except Exception as e:
        print "Error loading the file with exception %s" % e
    f.close()
    return new_z

if __name__ == "__main__":
    x = {"a": 1, "b": 2, "c": 3}
    y = [1,2,3,4,5,6]
    z = my_class()
    z.increase_a()

    filename = "json_start.cfg"
    explore_dumping(x, y, z, z, filename)    
    new_z = explore_loading(filename)

    print "Are the 2 objects equal?", z == new_z
    print ("Do they have the same attribute values? %s" 
           % (z.__dict__ == new_z.__dict__))
