""" Application of embedding a Mayavi scene in a TraitsUI: control the data
that is displayed.

Derived from Gael Varoquaux's demo:
http://docs.enthought.com/mayavi/mayavi/auto/example_mlab_interactive_dialog.html#example-mlab-interactive-dialog
"""
# Computation imports
from numpy.random import randn

# Traits and TraitsUI imports
#############################
from traits.api import HasTraits, Any, Button, Instance, on_trait_change, \
    Array
from traitsui.api import View, Item

# Mayavi imports
################
# Mayavi model
from mayavi.tools.mlab_scene_model import MlabSceneModel
# TraitsUI editor for a MlabSceneModel
from tvtk.pyface.scene_editor import SceneEditor
# Style of the scene editor
from mayavi.core.ui.mayavi_scene import MayaviScene
# Storage of a module (renderer)
from mayavi.core.api import PipelineBase

# Animation part
from pyface.timer.api import Timer

def compute_positions(N=3):
    """ Data generation: make random jumps from the present position
    """
    print "computing the positions"
    x = randn(N)
    y = randn(N)
    z = randn(N)
    return x, y, z

class BrownianMotionVisualization(HasTraits):

    scene = Instance(MlabSceneModel, ())
    plot = Instance(PipelineBase)
    x = Array()
    y = Array()
    z = Array()

    timer = Any()
    timer_button = Button()

    @on_trait_change('scene.activated')
    def create_plot(self):
        """ Wait before the scene is activated before trying to add data,
        modules, filers into it.
        """
        x, y, z = compute_positions()
        self.plot = self.scene.mlab.points3d(x, y, z)

    def _timer_button_fired(self):
        if self.timer is None:
            self.timer = Timer(100, self.update_plot)
        else:
            self.timer.stop()
            self.timer = None

    def update_plot(self):
        """ Recompute the ball positions and redraw
        """
        x, y, z = compute_positions()
        self.plot.mlab_source.set(x=x, y=y, z=z)


    # the layout of the dialog created
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                    height=250, width=300, show_label=False),
                Item('timer_button', label = "Start/Stop animation",
                      show_label = False),
                )

if __name__ == "__main__":
    vis = BrownianMotionVisualization()
    vis.configure_traits()
