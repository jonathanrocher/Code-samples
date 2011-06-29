# Standard library imports.
import logging

# Enthought library imports.
from enthought.envisage.ui.workbench.api import WorkbenchApplication
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
from enthought.plugins.ipython_shell.ipython_shell_plugin import IPythonShellPlugin

# Local imports
from dow_plugin import DowPlugin
from dow_ui_plugin import DowUIPlugin

# Logging.
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('dow_application.log', 'w')))
logger.setLevel(logging.DEBUG)

application = WorkbenchApplication(id='dow.application', name='Dow application',
    plugins=[
        CorePlugin(),
        WorkbenchPlugin(),
        IPythonShellPlugin(),
        DowPlugin(),
        DowUIPlugin(),
    ])
application.run()
