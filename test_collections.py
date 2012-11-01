# -*- coding: utf-8 -*-

from collections import *
from timeit import timeit

d = OrderedDict()
for i, key in enumerate('abcde'):
     d[key] = i+1
d["A"] = 0.
print d

