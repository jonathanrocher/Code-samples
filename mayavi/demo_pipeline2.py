""" Demo looking at a 3D scalar field 
"""
import numpy as np
from mayavi import mlab

x, y, z = np.ogrid[-10:10:20j, 
                   -10:10:20j, 
                   -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)
scalar_field = mlab.pipeline.scalar_field(s)
mlab.pipeline.volume(scalar_field)
mlab.show()