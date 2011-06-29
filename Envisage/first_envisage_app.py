"""
Simplest possible Envisage application that put together existing plugins
"""

# Applications
from enthought.envisage.ui.workbench.api import WorkbenchApplication

# Plugins.
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
from enthought.plugins.text_editor.text_editor_plugin import TextEditorPlugin
from enthought.plugins.ipython_shell.ipython_shell_plugin import IPythonShellPlugin

plugins = [ CorePlugin(), WorkbenchPlugin(), 
            TextEditorPlugin(), IPythonShellPlugin()]


def main():
    application = WorkbenchApplication(name = 'my IDE',
                                       id = 'practice.envisage.myide',
                                       plugins=plugins)
    application.run()

if __name__ == '__main__':
    main()
