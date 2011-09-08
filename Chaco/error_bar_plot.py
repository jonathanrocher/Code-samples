"""
Illustrate how to create an error bar plot.

Background: ErrorBarPlot is actually not really a plot object like Plot but an
XY renderer to overlay over a Plot. As a consquence, we dond't create an
Instance of a ErrorBarPlot and pass it arrays of values and errors. Instead
we can use the add_xy_plot method of a Plot object to render it.
"""
import numpy

# Enthought library imports
from enthought.traits.api import HasTraits, Instance
from enthought.traits.ui.api import View, Item

from enthought.chaco.api import ArrayDataSource, Plot, ArrayPlotData, \
    ErrorBarPlot
from enthought.enable.component_editor import ComponentEditor

def get_points():
    """
    Create the function x and y that has the errors
    """
    index = numpy.linspace(-5, 10, 40)
    data = numpy.cos(index)
    return index, data

def get_errors(value_points):
    """
    Create the errors
    """
    err_low = value_points - 0.3
    err_high = value_points + 0.3
    return err_low, err_high


class ErrorBarApp(HasTraits):
    """
    Class to embed the Error bar plot in an application
    """

    main_plot = Instance(Plot, args=())
    traits_view = View(Item("main_plot", editor = ComponentEditor(width = 500, 
                                                                  height = 500),
                            show_label = False),
                       width = 500, height = 500, resizable = True,
                       title = "My Application with a Chaco_plot")

    def __init__(self, *args, **kw):
        super(ErrorBarApp, self).__init__(*args, **kw)

        # Gather the values of the function and the error
        index_points, value_points = get_points()
        err_low, err_high = get_errors(value_points)
        # Converts to ArrayDataSource to feed the ErrorBarPlot class
        err_low, err_high = ArrayDataSource(err_low), ArrayDataSource(err_high)
        
        arrayplotdata = ArrayPlotData(index = index_points, value = value_points)
        plot = Plot(arrayplotdata)
        # Plot the function
        plot.plot(("index","value"), type = "line", color = "red")
        plot.title = "Cosine with errors"
        
        # Overlay the error bars: they are a 2D renderer.
        plot.add_xy_plot(index_name = "index", value_name = "value", 
                         renderer_factory = ErrorBarPlot,
                         value_low = err_low, value_high = err_high, 
                         # Below are optional configuration arguments
                         line_width = 2, color = "green", 
                         line_style = "solid", # could be 'dash', 'dot', ...
                         endcap_size = 5, 
                         endcap_style = "bar", # could be 'none'
                         
                         )
        self.main_plot =  plot


if __name__ == "__main__":
    myplot = ErrorBarApp()
    myplot.configure_traits()

