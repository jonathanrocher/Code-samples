""" Illustrate the use of generators for large processing pipelines. 
The pipeline involves 4 steps: identify the all files that have the 
word 'log' in their name, open all files based on their extension, 
process all lines in the file and retain the ones that contain python.
"""

import os
import gzip, bz2

def find_files(directory, part_name):
    print "Searching directory %s" % directory
    for path, directory, listfile in os.walk(directory):
        for name in listfile:
            if part_name in name:
                yield os.path.join(path, name)

def opener(filenames):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if ext == ".gz":
            f = gzip.open(filename)
        elif ext == ".bz2":
            f = bz2.BZ2File(filename)
        else:
            f = open(filename)
        yield f
        
def cat(filelist):
    for file_object in filelist:
        for line in file_object:
            yield line
    
def grep(string, lines):
    for line in lines:
        if string in line:
            yield line 
            
            
filenames = find_files(".", "log")
files = opener(filenames)
content = cat(files)
interesting_content = grep("python", content)

for line in interesting_content:
    print line