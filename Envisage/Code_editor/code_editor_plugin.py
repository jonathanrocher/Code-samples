from enthought.envisage.api import Plugin
from enthought.pyface.workbench.api import Perspective, PerspectiveItem
from enthought.traits.api import List

class CodeEditorPerspective(Perspective):
    name = 'iPython'
    enabled = True
    show_editor_area = True
    contents = [
        PerspectiveItem(id='enthought.plugins.python_shell_view'),
        #PerspectiveItem(id='enthought.logger.plugin.view.logger_view.LoggerView'),
        PerspectiveItem(id='enthought.plugins.text_editor_view'),
    ]

class CodeEditorPlugin(Plugin):
    """ Add a perspectives.
    """

    id = 'CodeEditorPlugin'

    PERSPECTIVES = 'enthought.envisage.ui.workbench.perspectives'
    
    perspectives = List(contributes_to=PERSPECTIVES)

    def _perspectives_default(self):
        return [CodeEditorPerspective]
