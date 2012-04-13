# -*- coding: utf-8 -*-
""" Demo for the usage of basemap to plot data onto a map of the Earth.

Author: Jonathan Rocher, Enthought Inc.
"""
import os, json, warnings

import numpy as np
from numpy.testing import assert_
from mpl_toolkits import basemap
from matplotlib.pyplot import figure, subplot, title, show, savefig, text

cylindrical_projection_list = ['mill', 'cyl', 'merc', 'gall']
pseudocylindrical_projection_list = ['ortho', 'moll', 'sinu', 'aeqd']
conical_projection_list = ['lcc', 'eqdc', 'aea']

# local mini db to get started. Add more entries manually using 
# http://www.travelmath.com/cities/
# Everytime a lookup is made in the large db, the local one is extended with the 
# result.
city_db = {# USA
               "austin, tx, us": ((30, 16, 0, 'N'),(97, 44, 34, 'W')), 
               "boulder, co, us": ((40, 0, 54, 'N'),(105, 16, 12, 'W')), 
               "new york, ny, us": ((40, 42, 51, 'N'),(74, 0, 23, 'W')),

           # Europe
               "paris, , fr": ((48, 52, 0, 'N'),(2, 20, 0, 'E')), 
               "london, , uk": ((51, 30, 0, 'N'),(0, 7, 0, 'W'))
               }


def deg_min_sec2deg(loc = (0,0,0,'N')):
    """ Convert a lat or lon in (deg, min, sec, orientation) into a decimal 
    degree value.
    """
    if isinstance(loc, float):
        # Already converted
        return loc
        
    # Deal with a sequence of locations
    if isinstance(loc[0], tuple) or isinstance(loc[0], list):
        return [deg_min_sec2deg(loc[i]) for i in range(len(loc))]
    
    (degs, mins, secs, orientation) = loc
    
    if orientation in ['W', 'S']:
        sign = -1
    elif orientation in ['E', 'N']:
        sign = 1
    else:
        raise ValueError("The orientation should be 'N', 'S', 'E', 'W' but %s "
                         "was passed." % orientation)
    
    result = sign * (degs + mins/60. + secs / 3600.)
    return result

def load_world_city_db():
    """ Load the world city db from http://www.maxmind.com/download/worldcities/
    """
    db_filename = "worldcities.txt"
    try:
        db = np.genfromtxt(db_filename, delimiter = ',', names = True, 
                            dtype = None, comments = "@")
    except IOError as e:
        raise IOError("File not found: download the file from "
                      "http://www.maxmind.com/download/worldcities/")
    return db

def get_coordinates_cities(cities, states = [""], countries = ["US"]):
    """ Convert a city name into a pair of coordinates. The state is optional 
    and can be given the value of None, or "".
    Everytime a city is looked up in the big db, the result is stored in the 
    local one.
    """
    # Validation
    assert(len(cities) == len(countries))

    # Initialization
    global city_db
    local_db_file = "local_city_db.json"
    if os.path.isfile(local_db_file):
        with open(local_db_file, "r") as f:
            city_db.update(json.load(f))
    world_city_db = None
    big_db_looked_up = False
    lats = []
    lons = []

    # Look-ups
    for i,city in enumerate(cities):
        country = countries[i]
        state = states[i]
        try:
            # Try in the local db first
            lat, lon = city_db["%s, %s, %s" % (city.lower(), state.lower(), 
                                                country.lower())]
            
        except KeyError as e:
            # City not in the local dict. Attempt to load the db from the file into 
            # a structured array
            print "Search the large db for", city, state, country
            if world_city_db is None:
                # Expensive !!
                world_city_db = load_world_city_db()
	    crit = ((world_city_db['City'] == city.lower()) 
                & (world_city_db['Country'] == country.lower()) 
                    & (world_city_db['Region'] == state.upper()))
            index = np.where(crit)[0]
            if len(index) != 1:
                raise ValueError("The number of cities with the criteria %s was"
    	                         " %s. Cannot proceed." 
    	                         % (city+", "+state+", "+country, len(index)))
            lon, lat = world_city_db[index]['Longitude'][0], world_city_db[index]['Latitude'][0]
            big_db_looked_up = True
            
        lons.append(lon)
        lats.append(lat)

    # clean up and memoize
    del world_city_db
    if big_db_looked_up:
        for i,city in enumerate(cities):
            country = countries[i]
            state = states[i]
            lat, lon = lats[i], lons[i]
            city_db["%s, %s, %s" % (city.lower(), state.lower(), country.lower())] = (lat,lon)
        with open(local_db_file, "w") as f:
            json.dump(city_db, f, indent=1)
            

    return lons, lats


def get_crnr_coordinates(region = "world"):
    """ Set the lower left and uper right corner coordinates used in a 
    cylindrical type projection.
    """
    if region == "world":
        llcrnrlon=-180
        urcrnrlon=180
        # Drawing the lats from -80 to 80 because mercator projection blows up 
        # at 90
        urcrnrlat=80
        llcrnrlat=-80
    elif region == "usa":
        llcrnrlon=-170
        urcrnrlon=-50
        urcrnrlat=75
        llcrnrlat=20
    elif region == "europe":
        llcrnrlon=-10
        urcrnrlon=40
        urcrnrlat=75
        llcrnrlat=35
        
    return  llcrnrlon, urcrnrlon, urcrnrlat, llcrnrlat


def get_conical_boundaries(region = "usa"):
    """ Compute the center point lat_0,lon_0 and 
    """
    if region == "usa":
        lat_0 = 50
        lon_0 = -107
        lat_1 = 45
        lat_2 = 55
        width=12000000
        height=9000000
    else:
        raise NotImplementedError("")
        
    return lat_0, lon_0, lat_1, lat_2, width, height


def explore_basemap_proj(region = "world", center = (30, -98), 
                         projection_type = "cyl", rolling_proj = True, 
                         resolution = 'c', style = 'bw', 
                         save_to_fig = False, **kw):
    """ Plot basemaps in various projections and around various point/region. 
    This has the goal of illustrating the usage of the basemap. The created 
    instance is returned for additional exploration.
    
    Inputs:
    =======
    region: string.
        Allowed values are "world", "usa", "europe", 
    style: string. 
        Allowed values are 'bw', 'color', 'bluemarble', 'shaderelief', 'etopo'

    """
    # Initialization
    llcrnrlon, urcrnrlon, urcrnrlat, llcrnrlat = None, None, None, None
    lat_0, lon_0, lat_1,lat_2, width, height = None, None, None, None, None, None
    
    # Set the desired lat and lon boundaries 
    if projection_type == "cyl":
        llcrnrlon, urcrnrlon, urcrnrlat, llcrnrlat = get_crnr_coordinates(region)
    elif projection_type == "pseudocyl":
        lat_0=center[0]
        lon_0=center[1]
    elif projection_type == "conical":
        lat_0, lon_0, lat_1, lat_2, width, height = get_conical_boundaries(region)
    else:
        raise ValueError("Unknown projection type")        
            
    figure()
    if projection_type == "cyl":
        projection_list = cylindrical_projection_list
    elif projection_type == "pseudocyl":
        projection_list = pseudocylindrical_projection_list
    elif projection_type == "conical":
        projection_list = conical_projection_list
    
    if rolling_proj:
        plot_line_num = len(projection_list)/3
        if len(projection_list)%3 != 0:
            plot_line_num += 1
	plot_col_number = min(len(projection_list), 3)
    else:
        plot_line_num, plot_col_number = (1,1)
        projection_list = [projection_list[0]]
        
    for i,proj in enumerate(projection_list):
        subplot(plot_line_num,plot_col_number,i)
        b = basemap.Basemap(projection=proj, resolution=resolution, 
                            # Corner coordinates
                            llcrnrlat=llcrnrlat,llcrnrlon=llcrnrlon,
                            urcrnrlat=urcrnrlat,urcrnrlon=urcrnrlon,
                            # Center coordinate
                            lat_0=lat_0, lon_0=lon_0, 
                            # Additional coordinate information
                            lat_1=lat_1, lat_2=lat_2, 
                            width=width, height=height, 
                            **kw)
        b.drawcoastlines(linewidth=1.25)
        b.drawcountries(linewidth=1.)
        if style != "bluemarble":
            # Don't draw the parallels and meridiens if blue marble because 
            # won't be visible
            b.drawparallels(np.arange(-90.,91.,20.), 
                            labels=[False,True,True,False])
            b.drawmeridians(np.arange(-180.,181.,20.),
                            labels=[True,False,False,True])
                            
        if projection_type in ["pseudocyl"]:
            b.drawmapboundary()
        if style == 'bluemarble':
            scales_res_mapping = {"c": 0.4, "l": 0.6, "i": 0.8, "h": 1, "f": 1}
            b.bluemarble(scale=scales_res_mapping[resolution])
        elif style == "etopo":
            b.etopo()
        elif style == "color":
            b.drawmapboundary(fill_color='aqua')
            b.fillcontinents(color = "coral", lake_color = 'aqua')
        elif style == "shaderelief":
            b.shadedrelief()
            
        title('Projection: %s' % proj)
    if save_to_fig:
        savefig("world_%s.png" % proj)
    return b


def add_point_data(bmp, x = [], y = [], lats = [], lons = [], style = 'ro', 
                   text_list = []):
    """ Add point passing their x,y map coordinates or their lat,lon 
    coordinates.
    """
    # Validation
    assert(len(x)==len(y))
    assert(len(lats) == len(lons))
    
    if lats:
        x,y = bmp(lons,lats)
        
    x,y = np.array(x), np.array(y)
    assert_(np.all(bmp.xmin <= x))
    assert_(np.all(x <= bmp.xmax))
    assert_(np.all(bmp.ymin <= y))
    assert_(np.all(y <= bmp.ymax))
    bmp.plot(x,y,style)
    
    if text_list:
        for i,text_el in enumerate(text_list):
            text(x[i]+100000,y[i]+100000,text_el.title())


if __name__ == "__main__":
    b = explore_basemap_proj(projection_type = "conical", region = "usa", 
                             resolution = "c", style = 'etopo', 
                             rolling_proj = False)
    
    lons = []
    lats = []
    
    # Collect locations of cities for the points
    cities = ["Austin", "Washington", "San Francisco"]
    states = ["TX", "DC", "CA"]
    countries = ["US", "US", "US"]
    labels = cities
    lons, lats = get_coordinates_cities(cities, states = states, countries = countries)
    # Convert to decimal values if necessary
    lons, lats = deg_min_sec2deg(lons), deg_min_sec2deg(lats)
    
    add_point_data(b, lats = lats, lons = lons, style = 'ro', 
                   text_list = labels)             
    show()
    