import pandas as pd
import matplotlib.pypolt as plt
import matplotlib.ticker as tkr


plt.style.use('ggplot')

def bar_h(dataframe, col, n = 12, title = None, xlabel='', save = False):   
    ax = dataframe.sort(col).tail(n)[col].plot(kind="barh", 
                                               figsize=[8, 5], 
                                               color='#B5022C', 
                                               width = 0.7, 
                                               grid=False)
                                               
    '''
    Function to draw a simple horizontal bar chart. Col can be one column of list of columns.
    Y-axis labels will be the dataframe index.
    '''
                                               
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('')
    ax.set_axis_bgcolor('white')
    ax.xaxis.grid(color = 'grey', linestyle='--')
    ax.xaxis.tick_bottom()
    
    # Format x-axis ticks with thousands separator
    x_format = tkr.FuncFormatter('{:,.0f}'.format)
    ax.xaxis.set_major_formatter(x_format)
    
    ax.yaxis.tick_left()
    ax.tick_params(axis="y", labelsize=12)
    plt.tight_layout()
    
    if save:
        file_name = title.replace(' ', '_') + '.png'
        plt.savefig(file_name, dpi=100)
    plt.show()