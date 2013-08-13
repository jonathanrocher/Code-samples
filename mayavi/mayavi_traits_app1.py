""" Next to the simplest Traits application containing a Mayavi scene where we
now offer a view of its engine in addition to the
"""
# Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Standard imports.
from numpy import sqrt, sin, mgrid

# Enthought imports.
from traits.api import HasTraits, Instance, Property
from traitsui.api import View, Item, HSplit, VSplit, InstanceEditor
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.core.ui.engine_view import EngineView
from mayavi.tools.mlab_scene_model import MlabSceneModel


######################################################################
class MayaviTraitsApp2(HasTraits):

    # The scene model.
    scene = Instance(MlabSceneModel, ())

    # The mayavi engine view.
    engine_view = Instance(EngineView)

    # The current selection in the engine tree view. This will be a pointing to
    # all kinds of objects inside the Mayavi pipeline and displaying its editor
    current_selection = Property

    ######################
    view = View(HSplit(VSplit(Item(name='engine_view',
                                   style='custom',
                                   resizable=True,
                                   show_label=False
                                   ),
                              Item(name='current_selection',
                                   editor=InstanceEditor(),
                                   enabled_when='current_selection is not None',
                                   style='custom',
                                   springy=True,
                                   show_label=False),
                                   ),
                               Item(name='scene',
                                    editor=SceneEditor(),
                                    show_label=False,
                                    resizable=True,
                                    height=500,
                                    width=500),
                        ),
                resizable=True,
                scrollable=True
                )

    def __init__(self, **traits):
        # Has to be done since it's a Traits class
        super(MayaviTraitsApp2, self).__init__(**traits)

        # Hook the engine view to the engine of the scene
        self.engine_view = EngineView(engine=self.scene.engine)

        # Hook up the current_selection to change when the one in the engine
        # changes.  This is probably unnecessary in Traits3 since you can show
        # the UI of a sub-object in T3.
        self.scene.engine.on_trait_change(self._selection_change,
                                          'current_selection')

        self.generate_data_mayavi()

    def generate_data_mayavi(self):
        from mayavi import mlab
        x, y = mgrid[-5:5:100j, -5:5:100j]
        r = sqrt(x**2 + y**2)
        z = 5*sin(r)/r
        mlab.surf(x, y, z)

    def _selection_change(self, old, new):
        self.trait_property_changed('current_selection', old, new)

    def _get_current_selection(self):
        return self.scene.engine.current_selection


if __name__ == '__main__':
    m = MayaviTraitsApp2()
    m.configure_traits()
