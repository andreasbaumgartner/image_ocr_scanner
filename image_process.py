# imports
import keras_ocr as keras_ocr
import matplotlib.pyplot as plt
import config
from config import logger

# import classes
from url_image import ImageUrlHealthCheck
from input_url import InputCheck

from image_plot import PlotImages

# Import Fake inputs
import fake_input


class KerasPred:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        # Load and Check Settings
        return self

    def __exit__(self):
        logger.info("KerrasMain Process exit")
        exit()  # TODO Check this function

    def check_input(self):
        url_count: int = InputCheck(self.url).check_multi_or_single()
        url_health: bool = ImageUrlHealthCheck(self.url).url_pass()

        if url_count != 0 and url_health == True:
            return True
        else:
            logger.warning(f"Input is False, {url_health} {self.url_count}")
            return False

    def load_images(self):
        pipeline = keras_ocr.pipeline.Pipeline()
        url_count: int = InputCheck(self.url).check_multi_or_single()

        # TODO Debug prints
        a = self.check_input()
        print("Check Input", a)
        b = url_count
        print("Url Count", b)

        if self.check_input() == True and url_count == 1:
            images = keras_ocr.tools.read(self.url)
            prediction_groups = pipeline.recognize(images)
            return images, prediction_groups

        elif self.check_input() == True and url_count > 1:
            print("elif triggered")
            images = [keras_ocr.tools.read(url) for url in self.url]
            prediction_groups = pipeline.recognize(images)
            return images, prediction_groups
        else:
            return None

    def process_img(self):
        print("Starting ...Processing")
        if self.load_images() != False:
            images, prediction_groups = self.load_images()
            fig, axs = PlotImages(images).image_plot()
            for ax, image, predictions in zip(axs, images, prediction_groups):
                keras_ocr.tools.drawAnnotations(
                    image=image, predictions=predictions, ax=ax
                )
            plt.show()


# Test Cases
url = [
    "https://images.unsplash.com/photo-1659599746931-09cff34dd307?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80"
]


a = KerasPred(url).load_images()
print(a)
