"""
Reading netCDF climate data and ploting it over the woldmap
"""
from os.path import join, dirname
import numpy as np
from netCDF4 import Dataset
from matplotlib.pyplot import figure, imshow, show
from mpl_toolkits.basemap import Basemap, shiftgrid

def print_content_info(filename):
    """ Load a netcdf filename and print out the metadata of the file.
    This gives you something kinda similar to ncdump.
    TODO: make it closer to ncdump
    """
    print "Opening netCDF file %s" % filename
    ncfile = Dataset(filename, mode='r')
    print "File format:", ncfile.file_format
    print "Metadata :"
    for attr in ncfile.ncattrs():
        print " "*4, attr, ":", getattr(ncfile,attr)
        
    print "Structure of the content:", ncfile.groups.keys()
    for child_grp in ncfile.groups.values():
        if child_grp.groups:
            print " "*8+"Content of %s is " % (child_grp, child_grp.groups)

    print "Dimensions defined at the top level:"
    for dim,val in ncfile.dimensions.items():
        print "    Dimension '%s' with length %s" % (dim, len(val))
    for child_grp in ncfile.groups.values():
        if child_grp.dimensions:
            for dim,val in ncfile.dimensions.items():
                print " "*8+"Dimension '%s' with length %s" % (dim, len(val))

    print "Variables in root group:"
    for var_name,val in ncfile.variables.items():
        print " "*4+"Variable '%s' of shape %s" % (var_name, val.shape)
        if val.ncattrs():
            print " "*4+"metadata: "
            for attr in val.ncattrs():
                print " "*8, attr, ":", getattr(val,attr)

    if ncfile.groups.values():
        print "Variables in other groups:"            
        for child_grp in ncfile.groups.values():
            if child_grp.variables:
                print " "*8+"Content of %: %s" % (child_grp, child_grp.variables)
            
    return ncfile

def extract_data(ncfile, sliced = False, lat_0=None, lon_0=None, spot = False):
    """ Extract a given variable and return a 2D array. Slice it to only select 
    the northern hemisphere if requested. If spot is True, extract only the 
    value located at (lat,lon)
    """
    relevant_array = ncfile.variables["207.210"]
    lat = ncfile.variables["latitude"]
    longit = ncfile.variables["longitude"]
    # The lat variables must be converted to a numpy array for the mask
    # to be an array instead of a boolean
    lat = np.array(lat)
    longit = np.array(longit)
    
    if sliced:
        slice_north_lat = (0 <= lat) & (lat <= 90)
        relevant_array = relevant_array[0, slice_north_lat, :]

    if spot:
        if lat_0 is None or lon_0 is None:
            raise ValueError("Requested the value in 1 location but didn't "
                             "provide a latitude and a longitude")
        mask_lat = lat == lat_0
        mask_long = longit == lon_0
        relevant_array = relevant_array[0, mask_lat, mask_long]

    return np.squeeze(relevant_array)

def plot_2Ddata(data_array):
    """ Plot of a 2D array.
    """
    figure()
    imshow(data_array, origin = 'upper')    
    return

def plot_2Ddata_with_underlay(data_array, lons=None, lats=None):
    """ Plot of a 2D array on top of coast lines and country lines.
    """
    figure()
    
    # Create the basemap instance and draw the continents
    # Basemap kw args: llcrnrlon = lower left corner longitude, and so on
    m = Basemap(llcrnrlon=-180, llcrnrlat=-90, urcrnrlon=180, urcrnrlat=90, projection='mill')
    m.drawcoastlines(linewidth=1.25)
    m.drawcountries(linewidth=0.5)
    #m.fillcontinents(color='0.8')
    m.drawparallels(np.arange(-90,91,20),labels=[1,1,0,0])
    m.drawmeridians(np.arange(-180,180,60),labels=[0,0,0,1])

    # Shift the data by 180 in longitude to center the map on longitude=0
    data_array, lon_out = shiftgrid(180, data_array, lons)

    # Add the data, and place origin in upper left since the origin of the numpy 
    # array corresponds tolat = 90 and long = 0
    m.imshow(data_array, origin = 'upper')

    # More complex version that involves interpolation on a grid of points in 
    # map coordinates.
    #nx = int((m.xmax-m.xmin)/500.)+1; ny = int((m.ymax-m.ymin)/500.)+1
    #dat_array = m.transform_scalar(data_array, lons,lats,nx,ny)
    #m.imshow(dat_array, origin = 'upper')
    
    
    #figure()
    #m = Basemap(projection='ortho',lon_0=-105,lat_0=40)
    #m.drawcoastlines(linewidth=1.25)
    #m.drawcountries(linewidth=0.5)
    #dat_transformed = m.transform_scalar(data_array, 

    return

if __name__ == "__main__":
    # 1. Provide a quick description of the content of the file
    script_location = dirname(__file__)
    ncfile = print_content_info(join(script_location, "climate.nc"))
    
    # 2. Extract and plot the entire 2D array of data
    lat = ncfile.variables["latitude"][:]
    longit = ncfile.variables["longitude"][:]
    print "Latitude range:", lat[0], lat[-1]
    print "Longitude range:", longit[0], longit[-1]
    full_data_image = extract_data(ncfile)
    plot_2Ddata(full_data_image)

    # 3. Extract and plot the data that is in the northern hemisphere only,
    # and print the data in Paris (lat = 48N, long = 2E)
    sliced_data_image = extract_data(ncfile, sliced = True)
    plot_2Ddata(sliced_data_image)

    print "In Paris, the measured value is", extract_data(ncfile, lat_0=48, 
                                                          lon_0=2, spot = True)

    # 4. Underlay the map of the world under the global image
    #lat.sort()
    plot_2Ddata_with_underlay(full_data_image, longit, lat)
    
    show()
