""" Simplest possible Traits application containing a Mayavi scene.

Uncomment the additional imports below to experiment with different available
editors (only the toolbar differs).
"""
# Standard imports.
from numpy import sqrt, sin, mgrid

# Enthought imports.
from traits.api import HasTraits, Instance
from traitsui.api import View, Item

from mayavi import mlab
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.tools.mlab_scene_model import MlabSceneModel

# Optional scene classes to use in the SceneEditor (see below)
# This one below is the most complete one with the Mayavi:
#from mayavi.core.ui.mayavi_scene import MayaviScene
# This one below is the most bare, just a vtk view:
#from tvtk.pyface.api import Scene


######################################################################
class MayaviTraitsApp(HasTraits):

    # The scene model.
    scene = Instance(MlabSceneModel, ())

    ######################
    view = View(Item(name='scene',
                        editor=SceneEditor(),
                        #editor=SceneEditor(scene_class=MayaviScene),
                        #editor=SceneEditor(scene_class=Scene),
                        show_label=False,
                        ),
                resizable=True,
                scrollable=True
                )

    def __init__(self, **traits):
        # Has to be done since it's a Traits class
        super(MayaviTraitsApp, self).__init__(**traits)

        x, y = mgrid[-5:5:100j, -5:5:100j]
        r = sqrt(x**2 + y**2)
        z = 5*sin(r)/r

        # Build the visualization of the data: specifying which Mayavi scene to
        # use is necessary
        mlab.surf(x, y, z, figure=self.scene.mayavi_scene)


if __name__ == '__main__':
    m = MayaviTraitsApp()
    m.configure_traits()
