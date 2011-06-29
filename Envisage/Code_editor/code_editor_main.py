# Standard library imports.
import logging

# Enthought library imports.
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
from enthought.plugins.ipython_shell.ipython_shell_plugin import IPythonShellPlugin
from enthought.logger.plugin.logger_plugin import LoggerPlugin
from enthought.plugins.text_editor.text_editor_plugin import TextEditorPlugin

# Local imports
from code_editor import CodeEditorApplication
from code_editor_plugin import CodeEditorPlugin

# Logging.
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('code_editor.log', 'w')))
logger.setLevel(logging.DEBUG)

application = CodeEditorApplication(
    id='code_editor', name='Code Editor',
    plugins=[
        CorePlugin(),
        WorkbenchPlugin(),
        IPythonShellPlugin(),
        LoggerPlugin(),
        TextEditorPlugin(),
        CodeEditorPlugin(),
    ])
application.run()
