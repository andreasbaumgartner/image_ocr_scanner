# imports
import matplotlib.pyplot as plt
import config


class PlotImages:
    def __inti__(self, images):
        self.images = images

    def image_plot(self):

        fig, axs = plt.subplots(nrows=len(self.images), figzize=config.FIGZIZE_IMAGE)
        return fig, axs
