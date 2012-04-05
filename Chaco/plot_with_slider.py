"""
Create the next to simplest chaco plot: separate the model and the view, and add 
a control on the model.
"""

from numpy import linspace, sin
from chaco.api import ArrayPlotData, Plot
from enable.component_editor import ComponentEditor

from traits.api import HasTraits, Instance, DelegatesTo, \
    on_trait_change, Array, Range
from traitsui.api import View, Item


class MyData(HasTraits):
    """ The model
    """
    x = Array()
    y = Array()
    param = Range(low=0, high=100)
    
    def __init__(self, param, *args, **kw):
        super(MyData, self).__init__(*args, **kw)
        self.param = param

    def _x_default(self):
        return linspace(-14,14,100)

    @on_trait_change('x, param')
    def compute_y(self):
        self.y = sin(self.param*self.x) * self.x**3


class MyPlot(HasTraits):
    """ The view
    """
    # The model
    data = Instance(MyData, ())
    # add a pointer to a parameter that we will want to control in the view
    param = DelegatesTo('data')
    
    # Plot object
    plot = Instance(Plot)
    # Data backing the plot
    plotdata = Instance(ArrayPlotData)
    
    traits_view = View(
            Item('param'),
            Item('plot', editor = ComponentEditor(), show_label = False),
                        width = 500, height = 500,
                        resizable = True, title = "My plot with a slider")
    
    def __init__(self, data, *args, **kw):
        """ Set up the view
        """
        self.data = data
        self.plotdata = ArrayPlotData(x=self.data.x,y=self.data.y)
        super(MyPlot, self).__init__(*args, **kw)
        

    def _plot_default(self):
        """ Set up the plot
        """
        # Create a plot and hook it up to the data it will represent
        plot = Plot(self.plotdata)
        # Add a line plot showing y as a function of x
        plot.plot(("x","y"), type = "line", color = "blue")
        plot.title = "param * sin(x)*x**3"
        return plot


    @on_trait_change('param')
    def update_plot_data(self,x,y):
        """ Update the data behind the plot. Since they are hooked, no need to 
        tell the plot to redraw.
        """
        self.plotdata.set_data("y", self.data.y)


if __name__ == "__main__":
    d = MyData(10)
    app_view = MyPlot(data = d)
    app_view.configure_traits()
