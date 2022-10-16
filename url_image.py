# imports
import requests

import config
from config import logger


class ImageUrlHealthCheck:
    """
    Check the Url that are give from the User and check the status_code $
    and the content-type.

    Function url_pass return True if the Health Check is right
    """

    def __init__(self, urls):
        self.urls = urls

    def check_url(self):
        status_code = []
        for url in self.urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    status_code.append(True)
                else:
                    logger.warning(f"Returned Status Code {response.status_code}")
                    status_code.append(False)
            except BaseException:
                return False
        if False not in status_code:
            return True

    def check_content(self, image_formats=config.IMAGE_FORMATS):
        status_list = []
        for url in self.urls:
            try:
                response = requests.head(url)
                if response.headers["content-type"] in image_formats:
                    status_list.append(True)
            except BaseException:
                status_list.append(False)
                continue

        if False not in status_list:
            return True

    def url_pass(self):
        if self.check_url() and self.check_content():
            return True
        else:
            logger.warning(f"URL NOT PASS HEALTH CHECK")
            return False
