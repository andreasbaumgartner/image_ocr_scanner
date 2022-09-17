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

    def __init__(self, url):
        self.url = url

    def check_url(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return True
        else:
            logger.warning(f"Returned Status Code {response.status_code}")
            return False

    def check_content(self, image_formats=config.IMAGE_FORMATS):
        response = requests.head(self.url)
        if response.headers["content-type"] in image_formats:
            return True
        else:
            return False

    def url_pass(self):
        if self.check_url() == True and self.check_content() == True:
            return True
        else:
            logger.warning(f"URL NOT PASS HEALTH CHECK")
            return False


# Test Cases Function
# test = "https://images.unsplash.com/photo-1659599746931-09cff34dd307?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80"
#
# s = ImageUrlHealthCheck(test).url_pass()
# print(s)
