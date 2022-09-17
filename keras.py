# imports
import keras_ocr
import config
from config import logger

class KerasMain:
    
    def __init__(self, images=images):
       self.images = images
    
    def __enter__(self, images=images):
        if not config.SKIP_SEARCH_IMAGES:
            self.load_images()
            logger.info(config.SKIP_SEARCH_IMAGES) 
        return self 
   
    def __exit__(self):
        self.exit()
        logger.info("KerrasMain Process exit") 
   

    def check_input():
        ...
   
    
    def load_images():
        ...
        
    
    def predict_images():
       ...  
        
    def return_plot():
        ...
       
