"""
Simplest possible Envisage application that put together existing plugins. 
This is the second version of it with a logger added and a perspective to 
layout default views. 

Note: For the perspective mechanism to work, the ini file of the project must 
be erased.
"""
# Std libraries
import logging

# Traits
from enthought.traits.api import List

# Applications
from enthought.envisage.ui.workbench.api import WorkbenchApplication

# Plugins.
from enthought.envisage.plugin import Plugin
from enthought.envisage.core_plugin import CorePlugin
from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
from enthought.plugins.text_editor.text_editor_plugin import TextEditorPlugin
from enthought.plugins.ipython_shell.ipython_shell_plugin import IPythonShellPlugin
from enthought.logger.plugin.logger_plugin import LoggerPlugin

# Perspective
from enthought.pyface.workbench.api import Perspective, PerspectiveItem


# Logger info for bug tracking
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('my_ide.log', 'w')))
logger.setLevel(logging.DEBUG)


class MyIDEPerspective(Perspective):
    """
    Specify a perspective for the default view of the application
    """
    name = 'Default View'
    enabled = True
    show_editor_area = True
    contents = [#PerspectiveItem(id='enthought.plugins.text_editor_view'),
                PerspectiveItem(id='enthought.plugins.python_shell_view',
                                position='bottom', relative_to='editor', 
                                style_hint='horizontal'),
                PerspectiveItem(id='enthought.logger.plugin.view.logger_view.LoggerView', 
                                position='with', relative_to= 
                                'enthought.plugins.python_shell_view', ),
                ]

class MyIDEPerspectivePlugin(Plugin):
    """
    A mini plugin to contribute the perspective to the application
    """
    id = "practice.envisage.myide.perspective_plugin"
    perspectives = List(contributes_to = 
                        'enthought.envisage.ui.workbench.perspectives')

    def _perspectives_default(self):
        return [MyIDEPerspective]

plugins = [ CorePlugin(), WorkbenchPlugin(), LoggerPlugin(),
            TextEditorPlugin(), IPythonShellPlugin(), 
            MyIDEPerspectivePlugin()]


def main():
    application = WorkbenchApplication(name = 'my IDE',
                                       id = 'practice.envisage.myide',
                                       plugins=plugins)
    application.run()

if __name__ == '__main__':
    main()
