""" Demo looking at a 3D scalar field 
"""
import numpy as np
from mayavi import mlab

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)
mlab.contour3d(s)
mlab.clf()
scalar_field = mlab.pipeline.scalar_field(s)
vol = mlab.pipeline.volume(scalar_field, vmin=0, vmax=0.8)
mlab.colorbar(orientation="vertical")
ipw_x = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                            plane_orientation='x_axes',
                            slice_index=10,
                        )
ipw_y = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                            plane_orientation='y_axes',
                           slice_index=10,
                        )
mlab.outline()
mlab.axes()
mlab.show()