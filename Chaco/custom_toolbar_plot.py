# Std lib
from numpy.random import randn

# For the toolbar plot
from chaco.api import ArrayPlotData, ToolbarPlot
from chaco.tools.toolbars.toolbar_buttons import IndexAxisLogButton,\
    ValueAxisLogButton, SaveAsButton
from chaco.tools.toolbars.plot_toolbar import PlotToolbar

# For the traits view
from traits.api import HasTraits, Type, Instance
from traitsui.api import View, Item
from enable.api import ComponentEditor

# For the custom button
from chaco.tools.toolbars.toolbar_buttons import ToolbarButton
from pyface.api import ImageResource
from kiva.image import Image

class LegendButton(ToolbarButton):
    label = 'Show/Hide legend'
    image = 'view-list-details'
    
    def __init__(self, *args, **kw):
        super(ToolbarButton, self).__init__(*args, **kw)
        image_resource = ImageResource(self.image)
        self._image = Image(image_resource.absolute_path)

    def perform(self, event):
        self.container.component.legend.visible \
                = not (self.container.component.legend.visible)
        self.container.request_redraw()        
        return

class MyToolbar(PlotToolbar):
    buttons = [ IndexAxisLogButton, ValueAxisLogButton,
                SaveAsButton, LegendButton ]

class MyPlot(HasTraits):
    toolbar_class = Type(MyToolbar)
    plot = Instance(ToolbarPlot)
    plot_data = Instance(ArrayPlotData)

    view = View(Item("plot", editor = ComponentEditor(), show_label = False),
                resizable = True)
    
    def __init__(self):
        x = randn(100); y = randn(100)
        self.plot_data = ArrayPlotData(x=x, y=y)
        self.plot = ToolbarPlot(self.plot_data,
                                toolbar_class=self.toolbar_class)
        self.plot.plot(("x", "y"), "scatter")

if __name__ == "__main__":
    mp = MyPlot()
    mp.configure_traits()
