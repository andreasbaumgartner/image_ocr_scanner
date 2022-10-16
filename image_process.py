# imports
import keras_ocr as keras_ocr
import matplotlib.pyplot as plt

pipeline = keras_ocr.pipeline.Pipeline()
import config
# Import Fake inputs
import fake_input
from config import logger
from image_plot import PlotImages
from input_url import InputCheck
# import classes
from url_image import ImageUrlHealthCheck


class KerasPred:
    def __init__(self, urls):
        self.urls = urls

    def __enter__(self):
        # Load and Check Settings
        return self

    def __exit__(self):
        logger.info("KerrasMain Process exit")
        exit()  # TODO Check this function

    def check_input(self):
        url_count: int = InputCheck(self.urls).check_multi_or_single()
        url_health: bool = ImageUrlHealthCheck(self.urls).url_pass()

        if url_count != 0 and url_health == True:
            return True
        else:
            logger.warning(f"Input is False, {url_health} {url_count}")
            return False

    def load_images(self):

        if self.check_input() == True:
            images: list = []
            for url in self.urls:
                image = keras_ocr.tools.read(url)
                images.append(image)
            prediction_groups = pipeline.recognize(images)
            return images, prediction_groups
        else:
            images: list = []
            prediction_groups = []
            return images, prediction_groups

    def process_img(self):
        if self.load_images() != 0:

            images, prediction_groups = self.load_images()
            fig, axs = PlotImages(images).image_plot()
            for ax, image, predictions in zip(axs, images, prediction_groups):
                keras_ocr.tools.drawAnnotations(
                    image=image, predictions=predictions, ax=ax
                )

            plt.show()


# Test Cases
test = [
    "https://images.unsplash.com/photo-1570822827176-d965104c7eb0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80",
    "https://images.unsplash.com/photo-1584447128309-b66b7a4d1b63?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1385&q=80",
]
a = KerasPred(test).process_img()
print(a)
