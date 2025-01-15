import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolor


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
    """
    Truncate a colormap.

    from https://stackoverflow.com/questions/40929467/how-to-use-and-plot-only-a-part-of-a-colorbar
    """
    if n == -1:
        n = cmap.N
    new_cmap = mcolor.LinearSegmentedColormap.from_list(
         'trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval),
         cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def plot_corr_matrix(corr, cmap=plt.cm.RdBu_r, trunc_cmap=True, cov=False, **imshow_kwds):
    """
    Plot a correlation matrix
    """
    if cov:
        std = np.sqrt(np.diag(corr))
        corr /= np.outer(std, std)

    cmap_min = 0.5 * (1 - np.min(corr)) + np.min(corr)
    if trunc_cmap:
        cmap = truncate_colormap(cmap, minval=cmap_min)
    plt.imshow(corr, cmap=cmap, **imshow_kwds)
