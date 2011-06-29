import logging

from enthought.envisage.ui.workbench.api import WorkbenchApplication    
from enthought.pyface.api import ImageResource, SplashScreen, AboutDialog

class CodeEditorApplication(WorkbenchApplication):
    """ The main Application class for the app.
    """

    def _about_dialog_default(self):
        """ Trait initializer. """
        about_dialog = AboutDialog(
            parent = self.workbench.active_window.control,
            image = ImageResource('about'),
            additions = ["Envisage Code Editor"]
        )
        return about_dialog

    def _splash_screen_default(self):
        """ Trait initializer. """
        splash_screen = SplashScreen(
            image = ImageResource('splash'),
            show_log_messages = False,
            log_level = logging.DEBUG,
        )
        return splash_screen
