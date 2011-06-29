
# Standard library imports.
import logging

# Enthought library imports.
from enthought.envisage.api import Application

# Logging.
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('my_first_application.log', 'w')))
logger.setLevel(logging.DEBUG)

application = Application(id='my.first.application',
    plugins=[])
application.run()
