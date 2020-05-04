import os
import logging

logger = logging.getLogger(__name__)

SAFE_EXTENSIONS = ['.txt', '.jpg', '.hocr', '.pdf']


def get_bool(key, default="NO"):
    """
    Returns True if environment variable named KEY is one of
    "yes", "y", "t", "true" (lowercase of uppercase)

    otherwise returns False
    """
    env_var_value = os.getenv(key, default).lower()
    YES_VALUES = ("yes", "y", "1", "t", "true")
    if env_var_value in YES_VALUES:
        return True

    return False


def safe_to_delete(place):
    if not os.path.exists(place):
        logging.warning(
            f"Trying to delete not exising folder"
            f" {place}"
        )
        return False

    for root, dirs, files in os.walk(place):
        for name in files:
            base, ext = os.path.splitext(name)
            if ext not in SAFE_EXTENSIONS:
                raise Exception("Trying to delete unsefe location")

    return True

