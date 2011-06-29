from enthought.traits.api import List
from enthought.pyface.workbench.api import TraitsUIView, Perspective, \
    PerspectiveItem
from enthought.envisage.api import Plugin

from dataset import Dataset

VIEWS = 'enthought.envisage.ui.workbench.views'
PERSPECTIVES = 'enthought.envisage.ui.workbench.perspectives'

class DowPerspective(Perspective):
    name = 'Dow'
    enabled = True
    show_editor_area = False
    contents = [
        PerspectiveItem(id='dow.dow_ui_plugin.dow_view'),
        PerspectiveItem(id='enthought.plugins.python_shell_view',
            position='bottom', relative_to='dow.dow_ui_plugin.dow_view'),
    ]

class DowUIPlugin(Plugin):
    name = 'Dow UI Plugin'
    id = 'dow.dow_ui_plugin'
    
    perspectives = List(contributes_to=PERSPECTIVES)

    def _perspectives_default(self):
        return [DowPerspective]

    views = List(contributes_to=VIEWS)

    def _views_default(self):
        return [self.create_dow_view]

    def create_dow_view(self, **traits):
        dow_data = self.application.get_service(Dataset,
            "name=='Dow Jones Industrial Average'")
    
        dow_view = TraitsUIView(
            id='dow.dow_ui_plugin.dow_view',
            name='Dow View',
            obj=dow_data,
            **traits
        )
            
        return dow_view

