import numpy
from dataset import Dataset

djia = Dataset(
    name='Dow Jones Industrial Average',
    data=numpy.loadtxt('dow.csv', delimiter=','),
)
djia.configure_traits()