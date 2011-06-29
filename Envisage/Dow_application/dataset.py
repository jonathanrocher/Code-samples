from enthought.traits.api import HasTraits, Str, Array
from enthought.traits.ui.api import View, Item
from enthought.traits.ui.ui_editors.array_view_editor import ArrayViewEditor

class Dataset(HasTraits):
    name = Str
    array = Array
    view = View(
        Item('name', style='readonly', show_label=False),
        Item('data', editor=ArrayViewEditor(),
            style='readonly', show_label=False),
        resizable=True, width=500, height=350,
    )