""" Most trivial demo of netCDF possible to illustrate how to write and read a netCDF file with netCDF4 package.
"""

from netCDF4 import *
import netCDF4

rootgrp = netCDF4.Dataset("test.nc", mode = "w")
ts_group = rootgrp.createGroup('timeseries')
rootgrp.createDimension('daily_sec_ts', size=3600)
rootgrp.createDimension('time', size=10)
storage = ts_group.createVariable('ts1','f8',dimensions =
                                      ('time', 'daily_sec_ts'))
for i in range(10):
    storage[i, :] = numpy.random.random((3600,))
rootgrp.sync()
rootgrp.close()

# Now reading
rootgrp = netCDF4.Dataset('test_data.nc', mode='r')
rootgrp = netCDF4.Dataset('test.nc', mode='r')
print rootgrp.file_format
ts_group = rootgrp.groups['timeseries']
ts1 = ts_group.variables['ts1']
print ts1.shape
print ts1[1:34]
