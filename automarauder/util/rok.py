
from ..images import *
from .automation import Automation
import logging

class ROK(Automation):

    # TODO: ADD RECONNECT / RESTART FOR WIFI DISCONNECTS
    
    @classmethod
    def isMarchOutside(cls) -> bool:
        '''Check if ANY march is currently outside of city.'''
        return cls.image_exists(MISC_MARCHES_OUT, confidence=0.9, timeout=0)
    
    @classmethod
    def exitPopups(cls) -> None:
        '''Exit any popup possibly blocking the screen by ESC button.\n
        Useful because popups can be different. MGE, Update Download, ETC.'''

        # 1: Attempt Closing
        cls.press_key("esc", 1)

        # 2: Close Profile if no popup was found (since ESC opens profile)
        if cls.image_exists(MISC_PROFILE_EXITGAME, confidence=0.9, timeout=0):
            cls.press_key("esc", 1)

    @classmethod
    def start_automarauder(
        cls,
    ) -> None:
        '''Attempt to start a new Marauder Run.'''

        cls.click_image(MARAUDER_SEARCH1, confidence=0.9, timeout=5, speed=1, delay=0.5)

        cls.click_image(MARAUDER_SEARCH2, confidence=0.9, timeout=5, speed=1, delay=0.5)

        if cls.click_image(MARAUDER_SEARCH3, confidence=0.9, timeout=5, speed=1, delay=0.5):
            logging.info("Started New Marauder Run.")

        if cls.click_image(MARAUDER_EXIT, confidence=0.9, timeout=5, speed=1, delay=0.5):
            logging.info("Exited Marauder Menu.")

    @classmethod
    def claim_system_rewards(
        cls,
    ) -> None:
        '''Claim all rewards from mail in the system category.'''

        cls.click_image(MAIL_OPEN, confidence=0.9, timeout=5, speed=1, delay=0.5)

        cls.click_image(MAIL_CATEGORY_SYSTEM, confidence=0.9, timeout=5, speed=1, delay=0.5)

        cls.click_image(MAIL_CLAIM_ALL, confidence=0.9, timeout=5, speed=1, delay=0.5)

        cls.click_image(MAIL_CONFIRM, confidence=0.9, timeout=5, speed=1, delay=0.5)

        cls.click_image(MAIL_CLOSE, confidence=0.9, timeout=5, speed=1, delay=0.5)

        logging.info("Claimed all system rewards.")
