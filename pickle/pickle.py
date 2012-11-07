import pickle

class MyInfo(object):
    name = "Jonathan Rocher"
    age = 31
    Address = {"street": "Rip Ford Dr",
               "Number": 3614,
               "City": "Austin"}
    
def save2file(object, filename):
    file = open(filename,'wb')
    pickle.dump(object, file, protocol = 2)
    file.close()
    
def recover_from_file(filename):
    file = open(filename,'rb')
    obj = pickle.load(file)
    file.close()
    return obj


if __name__ == "__main__":
    info = MyInfo()
    filename = "myinfo.pkl"
    save2file(info,filename)
    new_obj = recover_from_file(filename)
    print "Object recovered is identical?", new_obj.__dict__ == info.__dict__
