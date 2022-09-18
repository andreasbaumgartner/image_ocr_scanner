# imports
import keras_ocr as keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()
import config
from config import logger

# import classes
from url_image import ImageUrlHealthCheck
from input_url import InputCheck

from image_plot import PlotImages

# Import Fake inputs
import fake_input


class KerasPred:
    def __init__(self, urls):
        self.urls = urls

    def __enter__(self):
        # Load and Check Settings
        return self

    def __exit__(self):
        exit()  # TODO Check this function
        logger.info("KerrasMain Process exit")

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


# Test Cases
test = [
    "https://images.unsplash.com/photo-1659599746931-09cff34dd307?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80",
    "https://images.unsplash.com/photo-1659976400255-d5cca2c2234a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1364&q=80",
]
a = KerasPred(test).load_images()
print(a)
