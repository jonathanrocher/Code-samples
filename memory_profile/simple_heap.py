""" Simple class to track down the memory usage of an object, including the 
objects it points to that are likely to be part of the object.

Based on an original version by Robert Kern
"""
from collections import deque
import gc
import sys
import types

from traits.api import Any, HasTraits, Int, Set
from numpy import ndarray, dtype

class SimpleHeap(HasTraits):
    """ A simple heap memory tracker.
    """

    # The root object we are trying to ascertain the size of.
    root = Any()

    # The total size of the rooted object graph.
    size = Int()

    # The IDs of objects that have been seen.
    _seen = Set(Int)

    def __init__(self, root, **traits):
        super(SimpleHeap, self).__init__(root=root, **traits)

        self.compute_size()

    def compute_size(self):
        queue = deque([self.root])
        while queue:
            self.size += self._pop_and_size(queue)
        print "Size of the object and what it contains is %s bytes." % self.size

    def _pop_and_size(self, queue):
        """ Pop an item off the queue and return its size. Add its referents to 
        the queue.
        """
        obj = queue.popleft()
        if id(obj) in self._seen:
            return 0
        else:
            self._seen.add(id(obj))
        if isinstance(obj, ndarray):
            # The elements of a numpy array are not seen by the gc as a referent
            container_size = sys.getsizeof(obj)
            if obj.dtype != dtype('object'): 
                return container_size + obj.nbytes
            else:
                # In this case, the element is a pointer (4 bytes). 
                # Convert to a list to find the referents.
                referents = self._filtered_referents(obj.tolist())
                queue.extend(referents)
                return container_size
        else:
            size = sys.getsizeof(obj)
            referents = self._filtered_referents(obj)
            queue.extend(referents)
        return size

    @staticmethod
    def _filtered_referents(obj):
        """ Return the referents of an object that we consider as "part"
        of the object using the garbage collector.
        """
        referents = gc.get_referents(obj)
        badtypes = (types.CodeType, types.ModuleType, types.FunctionType,
            types.ClassType, types.TypeType, types.FrameType,
            types.GeneratorType, types.GetSetDescriptorType, types.LambdaType,
            types.MemberDescriptorType, types.MethodType, types.TracebackType,
            types.UnboundMethodType)
        good = [x for x in referents if not isinstance(x, badtypes)]
        return good