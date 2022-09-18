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
        print("Starting Check Url")
        status_code = []
        for url in self.urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    status_code.append(True)
                else:
                    logger.warning(f"Returned Status Code {response.status_code}")
                    status_code.append(False)
            except:
                return False
        if False not in status_code:
            return True

    def check_content(self, image_formats=config.IMAGE_FORMATS):
        print("Starting Check...")
        status_list = []
        for url in self.urls:
            try:
                response = requests.head(url)
                if response.headers["content-type"] in image_formats:
                    status_list.append(True)
            except:
                status_list.append(False)
                continue

        if False not in status_list:
            return True

    def url_pass(self):
        print("Starting Url_pAss..")
        if self.check_url() == True and self.check_content() == True:
            return True
        else:
            logger.warning(f"URL NOT PASS HEALTH CHECK")
            return False


# Test Cases Function
test = [
    "https://images.unsplash.com/photo-1659599746931-09cff34dd307?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=872&q=80",
    "https://images.unsplash.com/photo-1659976400255-d5cca2c2234a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1364&q=80",
]


s = ImageUrlHealthCheck(test).url_pass()
print(s)
