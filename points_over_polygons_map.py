import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import fiona
from itertools import chain

'''

Recipe to plot x, y points over a shapefile. It requires two things from the user:
A path to a shapefile, and lists of latitude and longitude points.

If using pandas Series, convert to list first. 

e.g. lons = df.lon.tolist()

'''

shapefile = '/path/to/shapefile/'

lats = '[list of latitudes]'
lons = '[list of longitudes]'

# Get map bounds from shapefile with Fiona
shp = fiona.open(shapefile + '.shp')
bds = shp.bounds
shp.close()
extra = 0.01
ll = (bds[0], bds[1])
ur = (bds[2], bds[3])
coords = list(chain(ll, ur))
w, h = coords[2] - coords[0], coords[3] - coords[1]

# Define main basemap. Attention to lon_0 and lat_0 params
m = Basemap(
    projection='tmerc',
    lon_0= -73.6,  # For Mercator projetion, need to supply center lat and lon
    lat_0= 45.5,
    ellps = 'WGS84',
    llcrnrlon=coords[0] - extra * w,
    llcrnrlat=coords[1] - extra + 0.01 * h,
    urcrnrlon=coords[2] + extra * w,
    urcrnrlat=coords[3] + extra + 0.01 * h,
    lat_ts=0,
    resolution='i',
    suppress_ticks=True)

plt.figure(figsize=[15, 10])

# Read the shapefile
m.readshapefile(
    shapefile,
    'shapefile_name',
    color='coral',
    zorder=2)

# Plot the points over the shapefile
x, y = m(lons, lats)
m.plot(x, y, 'bo', markersize=3)

plt.show()