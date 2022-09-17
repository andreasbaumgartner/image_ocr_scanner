# imports
import matplotlib.pyplot as plt
import config


class PlotImages:
    def __init__(self, images):
        self.images = images

    def image_plot(self):

        fig, axs = plt.subplots(nrows=len(self.images), figsize=config.FIGSIZE_IMAGE)

        return fig, axs
