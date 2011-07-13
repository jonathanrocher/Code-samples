# Standard library imports.
import logging

## Toolkit
# Line below added to make sure enthought.qt.__init__ is run early enough 
# to avoid conflicts with other imports.
import enthought.qt
from enthought.etsconfig.api import ETSConfig
ETSConfig.toolkit='qt4'
QT_API = 'pyqt'
#QT_API = 'pyside'

# Plugin imports.
from envisage.core_plugin import CorePlugin
from envisage.ui.tasks.tasks_plugin import TasksPlugin
from attractors_plugin import AttractorsPlugin

# Local imports.
from attractors_application import AttractorsApplication


def main(argv):
    """ Run the application.
    """
    logging.basicConfig(level=logging.WARNING)

    plugins = [ CorePlugin(), TasksPlugin(), AttractorsPlugin() ]
    app = AttractorsApplication(plugins=plugins)
    app.run()

    logging.shutdown()


if __name__ == '__main__':
    import sys
    main(sys.argv)
