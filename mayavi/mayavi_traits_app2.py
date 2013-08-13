""" Application of embedding a Mayavi scene in a TraitsUI: control the data
that is displayed.

Derived from Gael Varoquaux's demo:
http://docs.enthought.com/mayavi/mayavi/auto/example_mlab_interactive_dialog.html#example-mlab-interactive-dialog
"""
# Computation imports
from numpy import linspace, pi, cos, sin

# Traits and TraitsUI imports
#############################
from traits.api import HasTraits, Range, Instance, on_trait_change
from traitsui.api import View, Item, HGroup

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

def curve(n_mer, n_long):
    """ Data generation
    """
    phi = linspace(0, 2*pi, 2000)
    return [ cos(phi*n_mer) * (1 + 0.5*cos(n_long*phi)),
            sin(phi*n_mer) * (1 + 0.5*cos(n_long*phi)),
            0.5*sin(n_long*phi),
            sin(phi*n_mer)]

class Visualization(HasTraits):
    meridional = Range(1, 30,  6)
    transverse = Range(0, 30, 11)
    scene      = Instance(MlabSceneModel, ())
    plot = Instance(PipelineBase)

    @on_trait_change('scene.activated')
    def create_plot(self):
        """ Wait before the scene is activated before trying to add data,
        modules, filers into it.
        """
        x, y, z, t = curve(self.meridional, self.transverse)
        self.plot = self.scene.mlab.plot3d(x, y, z, t, colormap='Spectral')

    @on_trait_change('meridional,transverse')
    def update_plot(self):
        """ Recompute the data
        """
        x, y, z, t = curve(self.meridional, self.transverse)
        self.plot.mlab_source.set(x=x, y=y, z=z, scalars=t)


    # the layout of the dialog created
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                    height=250, width=300, show_label=False),
                HGroup(
                        '_', 'meridional', 'transverse',
                    ),
                )

if __name__ == "__main__":
    visualization = Visualization()
    visualization.configure_traits()
