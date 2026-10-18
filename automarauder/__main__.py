import logging

logging.basicConfig(
    level=logging.INFO,  # levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ],  # logging.FileHandler(PATH, mode="a", encoding="utf-8")
)

logger = logging.getLogger(__name__)

from .main import main as automarauder

if __name__ == "__main__":
    try:
        automarauder()

    except KeyboardInterrupt:
        logger.info("Shutting down...")
        logging.shutdown()
