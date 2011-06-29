""" 
A simple example of using Tasks. This module creates a pure pyface GUI 
application from a task. This is the cheapest way to create a gui from 
a task.
"""

#toolkits
import enthought.qt
from enthought.etsconfig.api import ETSConfig
# Select the toolkit to use:
ETSConfig.toolkit='qt4'
if ETSConfig.toolkit == 'qt4':
    QT_API = 'pyqt'

# Enthought library imports.
from pyface.api import GUI
from pyface.tasks.api import TaskWindow

# Local imports.
from example_task import ExampleTask

def main(argv):
    # Create the GUI (this does NOT start the GUI event loop).
    gui = GUI()

    # Create a Task and add it to a TaskWindow.
    task = ExampleTask()
    window = TaskWindow(size=(800, 600))
    window.add_task(task)

    # Show the window.
    window.open()

    # Start the GUI event loop.
    gui.start_event_loop()


if __name__ == '__main__':
    import sys
    main(sys.argv)

