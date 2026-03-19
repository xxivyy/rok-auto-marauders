
import logging

logging.basicConfig(
    level=logging.INFO, # levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()], # logging.FileHandler(PATH, mode="a", encoding="utf-8")
)

import os
import sys
from .main import main as automarauder

if __name__ == "__main__":

    args = sys.argv[1:]
    
    try:
        automarauder(args)

    except KeyboardInterrupt:
        logging.info("Shutting down...")
        os._exit(1)
