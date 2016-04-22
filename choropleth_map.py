import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
from pysal.esda.mapclassify import Natural_Breaks as nb


def make_choro(shapefile, dataframe, val_col, index_col, num_breaks = 6, color_ramp = 'Greens' title = '', main_poly = None, save = False):
    """
    Makes a choropelth map of a given shapefile and a numerical column of a dataframe. Shapefile and
    dataframe must both have a matching index_column for joining. Uses Jenks natural breaks for 
    classifying.
    
    Based on this tutorial: http://ramiro.org/notebook/basemap-choropleth/
    """

	num_colors = num_breaks
	cm = plt.get_cmap(color_ramp)
	scheme = [cm(i / num_colors) for i in range(num_colors)]
    
    # Create bins for color values
    breaks = nb( dataframe[val_col], initial=150, k = num_colors - 1)
    bins = breaks.bins
    frame['bin'] = np.digitize(dataframe[val_col], bins) 

    mpl.style.use('ggplot')
    fig = plt.figure(figsize=(22, 12))

    ax = fig.add_subplot(111, axisbg='w', frame_on=False)
    fig.suptitle('Map of {}'.format(title), fontsize=30, y=.95)
    
    m = Basemap(lon_0=0, projection='robin')
    m.drawmapboundary(color='w')
    
    m.readshapefile(shapefile, 'units', color='#444444', linewidth=.2)   
    for info, shape in zip(m.units_info, m.units):
        idx = info[index_col]
        if idx not in frame.index:
            color = '#dddddd'
    '''
    Optional for coloring a single polygon differently        
        elif idx == main_poly:
            color = '#E6A3B1'
    '''
        else:
            color = scheme[dataframe.ix[idx]['bin']]

        patches = [Polygon(np.array(shape), True)]
        pc = PatchCollection(patches)
        pc.set_facecolor(color)
        ax.add_collection(pc)

    # Cover up bottom (Antarctica if world map) so legend can be placed over it.
    ax.axhspan(0, 1000 * 1800, facecolor='w', edgecolor='w', zorder=2)

    # Draw color legend.
    ax_legend = fig.add_axes([0.35, 0.19, 0.3, 0.03], zorder=3)
    cmap = mpl.colors.ListedColormap(scheme)
    cb = mpl.colorbar.ColorbarBase(ax_legend, cmap=cmap, ticks=bins, boundaries=bins, orientation='horizontal')
    cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])
    if save:
        save_name = title.replace(' ', '_') + '.png'
        plt.savefig(save_name, dpi=100)