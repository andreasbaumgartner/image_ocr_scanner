# imports
import keras_ocr as keras_ocr

import config
from config import logger

# import classes
from url_image import ImageUrlHealthCheck
from input_url import InputCheck
import fake_input


class KerasPred:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        # Load and Check Settings
        return self

    def __exit__(self):
        exit()  # TODO Check this function
        logger.info("KerrasMain Process exit")

    def check_input(self):
        url_count: int = InputCheck(self.url).check_multi_or_single()
        url_health: bool = ImageUrlHealthCheck(self.url).url_pass()

        if url_count != 0 and url_health == True:
            return True
        else:
            logger.warning(f"Input is False, {url_health} {url_count}")
            return False

    def load_images(self):

        if self.check_input() == True:
            images = keras_ocr.tools.read(self.url)
            prediction_groups = keras_ocr.pipeline.Pipeline(recognizer=images)
            return images, prediction_groups
        else:
            return False


# Test Cases
url = "https://images.unsplash.com/photo-1659599746931-09cff34dd307?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80"
a = KerasPred(url).load_images()
print(a)
