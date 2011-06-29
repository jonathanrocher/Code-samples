import numpy

from enthought.traits.api import Instance, List
from enthought.envisage.api import Plugin, ServiceOffer

from dataset import Dataset

SERVICE_OFFERS = 'enthought.envisage.service_offers'
BINDINGS = 'enthought.plugins.python_shell.bindings'    

class DowPlugin(Plugin):
    name = 'Dow Plugin'
    id = 'dow.dow_plugin'

    djia = Instance(Dataset)

    service_offers = List(contributes_to=SERVICE_OFFERS)

    def _service_offers_default(self):
        return [
            ServiceOffer(protocol=Dataset, factory=self.dow_factory),
        ]

    bindings = List(contributes_to=BINDINGS)
    
    def _bindings_default(self):
        """ Bindings for the (i)python shell."""
        
        return [{'djia': self.djia}]

    def dow_factory(self):
        return self.djia

    def start(self):
        self.djia = Dataset(
            name='Dow Jones Industrial Average',
            data=numpy.loadtxt('dow.csv', delimiter=','),
        )