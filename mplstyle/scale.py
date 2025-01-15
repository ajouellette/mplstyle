import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.scale as mscale
import matplotlib.ticker as ticker


class SquareRootScale(mscale.ScaleBase):
    """
    ScaleBase class for generating a square root scale.

    use: ax.set_xscale("sqrt")
    see also: https://stackoverflow.com/questions/42277989/square-root-scale-using-matplotlib-python
    """

    name = "sqrt"

    def __init__(self, axis):
        forward = lambda x: np.sqrt(x)
        inverse = lambda x: x**2
        transform = mscale.FuncTransform(forward, inverse)
        self._transform = transform

    def get_transform(self):
        return self._transform

    def set_default_locators_and_formatters(self, axis):
        axis.set_major_locator(ticker.AutoLocator())
        axis.set_major_formatter(ticker.ScalarFormatter())
        axis.set_minor_formatter(ticker.NullFormatter())
        # update the minor locator for x and y axis based on rcParams
        if (axis.axis_name == 'x' and mpl.rcParams['xtick.minor.visible'] or
                axis.axis_name == 'y' and mpl.rcParams['ytick.minor.visible']):
            axis.set_minor_locator(ticker.AutoMinorLocator())
        else:
            axis.set_minor_locator(ticker.NullLocator())

    def limit_range_for_scale(self, vmin, vmax, minpos):
        return  max(0., vmin), vmax


mscale.register_scale(SquareRootScale)
