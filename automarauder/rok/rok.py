import logging
import time

from ..images import *
from .automation import Automation

logger = logging.getLogger(__name__)


class ROK(Automation):
    """ROK Main Functionality."""

    @classmethod
    def _is_march_outside(cls) -> bool:
        """Check if ANY march is currently outside of city."""
        return cls.image_exists(MISC_MARCHES_OUT, confidence=0.8)

    @classmethod
    def attempt_reconnect(cls) -> bool:
        if cls.image_exists(MISC_DISCONNECTED):
            cls.click_image(MISC_DISCONNECTED_CONFIRM)
            return True
        return False

    @classmethod
    def exit_popups(cls) -> None:
        """Exit any popup possibly blocking the screen by ESC button.\n
        Useful because popups can be different. MGE, Update Download, ETC."""

        if cls.attempt_reconnect():
            return

        # 1: Attempt Closing
        cls.press_key("esc", 1)

        # 2: Close Profile if no popup was found (since ESC opens profile)
        if cls.image_exists(MISC_PROFILE_EXITGAME):
            cls.press_key("esc", 1)

        logger.info("Potentially closed Popup.")
        time.sleep(3)

    @classmethod
    def start_automarauder(
        cls,
    ) -> None:
        """Attempt to start a new Marauder Run."""

        if ROK._is_march_outside():
            return

        found_search1 = cls.click_image(MARAUDER_SEARCH1, timeout=2)
        found_search2 = cls.click_image(MARAUDER_SEARCH2, timeout=2)

        if not all([found_search1, found_search2]):
            cls.exit_popups()
            return  # cancel marauder attempt if something was in the way.

        if cls.click_image(MARAUDER_SEARCH3, timeout=2):
            logger.info("Started New Marauder Run.")

        elif cls.click_image(MARAUDER_EXIT, timeout=2):
            logger.info("Exited Marauder Menu.")

    @classmethod
    def claim_system_rewards(
        cls,
    ) -> None:
        """Claim all rewards from mail in the system category."""

        while True:
            found_open = cls.click_image(MAIL_OPEN, timeout=2)

            cls.click_image(MAIL_CATEGORY_SYSTEM, timeout=2)

            found_claim = cls.click_image(MAIL_CLAIM_ALL, timeout=2)

            if not all([found_open, found_claim]):
                cls.exit_popups()
            else:
                break  # break out of loop only if success. collecting mail is important.

        cls.click_image(MAIL_CONFIRM, timeout=2)

        cls.click_image(MAIL_CLOSE, timeout=2)

        logger.info("Claimed all system rewards.")
