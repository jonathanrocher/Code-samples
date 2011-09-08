"""
Create the simplest possible static Chaco plot.

Deriving from HasTraits the new class can use all the power
of Traits and the super() in its constructor makes sure this
object possesses the attributes and methods of its parent class.
"""

from enthought.chaco.api import ArrayPlotData, Plot
from enthought.enable.component_editor import ComponentEditor

from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item

class MyPlot(HasTraits):
    plot = Instance(Plot)
    
    traits_view = View(Item('plot', editor = ComponentEditor(), show_label = False),
                       width = 500, height = 500,
                       resizable = True, title = "My line plot")

    def __init__(self, x,y, *args, **kw):
        super(MyPlot, self).__init__(*args, **kw)
        plotdata = ArrayPlotData(x=x,y=y)
        plot = Plot(plotdata)
        plot.plot(("x","y"), type = "line", color = "blue")
        #other possible types: "scatter",  polygon, cmap_scatter,
        # img_plot, cmap_img_plot = CMapImagePlot, contour_line_plot,
        # contour_poly_plot, candle
        plot.title = "sin(x)*x**3"
        self.plot = plot


if __name__ == "__main__":
    from numpy import linspace, sin

    x = linspace(-14,14,100)
    y = sin(x) * x**3
    lineplot = MyPlot(x,y)
    lineplot.configure_traits()
