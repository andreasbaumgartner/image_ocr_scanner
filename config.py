# Config File for Settings
import logging

# logging basic config
logging.basicConfig(
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
    format="%(asctime)s [%(levelname).4s] %(message)s",
    datefmt="%a %d %H:%M:%S",
)
# define logger
logger = logging.getLogger()

# --------------# Settings

# Img formats which are supported
IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg")

# DEFINE USE FAKE INPUT
FAKE_INPUT = True

# DEFINE FIGZIZE IMAGE FOR PLOT
FIGSIZE_IMAGE = (20, 20)
