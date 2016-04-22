import pandas as pd
import matplotlib.pypolt as plt

plt.style.use('ggplot')

def scatter_plot(dataframe, x, y, title='', xlabel='', ylabel='', color='g', ylim=None, save=False):
    ax = dataframe.plot(kind='scatter', figsize=[7, 7], x = x, y = y, color=color, 
                        edgecolor="k", ylim=ylim )
    ax.set_title(title)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    if save:
        save_name = title.replace(' ', '_') + '.png'
        plt.savefig(save_name, dpi=100)
    plt.show()  