""" Demo of making an animation with matplotlib. This is the simplest possible
option: just redrawing different things on the same figure at a given interval.

Alternatives to this require a timer or an instance of the animation subpackage
in MPL. See animation_demo.py for the timer and animation_demo and
matplotlib.animation and animation_demo*.py for the animation subpackage.

Note: this should be run outside of ipython, to avoid interference.
"""
import numpy as np
from time import sleep
from matplotlib.pyplot import show, ion, figure
# Allow show() to be non-blocking
ion()

x = np.linspace(0, 4*np.pi)
fig = figure()

for phase in np.linspace(0, 2*np.pi):
    y = np.sin(x+phase)
    ax = fig.add_subplot(1,1,1)
    line, = ax.plot(x, y)
    # Force a redraw
    ax.figure.canvas.draw()
    sleep(0.5)
    show()
