""" Demo 2 of a timer and an animation using matplotlib: this time the 
Note: crashes on WX but works with the QT backend. 
""" 

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(0, 20)
y = 0.5 * x * x
line, = ax.plot(x, y)

# The class only takes a line object as a parameter. All
# of the needed information is obtained from the object itself.
class updatingLine(object):
    def __init__(self, line):
        self._line = line
        self._xdata = line.get_xdata()
        self._ydata = line.get_ydata()
        self.counter = 0
        self.canvas = line.figure.canvas

    def __call__(self):
        self._line.set_data(self._xdata[:self.counter],
            self._ydata[:self.counter])
        self.canvas.draw()
        self.counter = (self.counter + 1) % self._xdata.size

timer = fig.canvas.new_timer(interval=100)
timer.add_callback(updatingLine(line))
timer.start()