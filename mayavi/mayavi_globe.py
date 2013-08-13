""" Simulating a globe with the continents drawn.
"""

from mayavi import mlab
from mayavi.sources.builtin_surface import BuiltinSurface

ocean_blue = (0.4, 0.5, 1.0)
r = 6371 # km

sphere = mlab.points3d(0, 0, 0, name='Globe',
  scale_mode='none', scale_factor=r * 2.0,
  color=ocean_blue, resolution=50)

sphere.actor.property.specular = 0.20
sphere.actor.property.specular_power = 10

continents_src = BuiltinSurface(source='earth', name='Continents')
continents_src.data_source.on_ratio = 1  # detail level
continents_src.data_source.radius = r
continents = mlab.pipeline.surface(continents_src, color=(0, 0, 0))
mlab.show()
