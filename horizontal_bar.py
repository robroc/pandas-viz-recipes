import pandas as pd
import matplotlib.pypolt as plt

plt.style.use('ggplot')

def bar_h(dataframe, col, n = 12, title = '', xlabel='', save = False):
    '''
    Function to draw a simple horizontal bar chart. Col can be one column of list of columns.
    Bar labels will be the dataframe index.
    '''
    
    ax = dataframe.sort(col).tail(n)[col].plot(kind='barh', figsize=[8, 5])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('')
    if save:
        save_name = title.replace(' ', '_') + '.png'
        plt.savefig(save_name, dpi=100)
    plt.show()