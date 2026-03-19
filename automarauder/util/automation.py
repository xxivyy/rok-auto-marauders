
import os
import time
import pyautogui

class Automation:

    @classmethod
    def click_image(
        cls,
        image: os.PathLike,
        confidence: float = 0.9,
        timeout: float = 0,
        speed: float = 0,
        delay: float = 0,
        region: tuple[int, int, int, int] | None = None,
        throw: bool = False,
    ) -> bool:
        
        try:
            _image = pyautogui.locateOnScreen(
                image, 
                minSearchTime=timeout,
                region=region,
                confidence=confidence,
                )
        except:
            if throw: raise Exception(f"Image not found: {image}")
            return False
        
        _image_center = pyautogui.center((_image.left, _image.top, _image.width, _image.height))

        pyautogui.moveTo(
            x=_image_center.x,
            y=_image_center.y,
            duration=speed,
            # optional: custom tween
        )

        time.sleep(delay)
        pyautogui.click()
        return True

    @classmethod
    def image_exists(
        cls,
        image: os.PathLike,
        confidence: float = 0.9,
        timeout: float = 0,
        region: tuple[int, int, int, int] | None = None,
        throw: bool = False,
    ) -> bool:
        
        try:
            pyautogui.locateOnScreen(
                image=image,
                minSearchTime=timeout,
                confidence=confidence,
                region=region,
            )
            return True
        except:
            if throw: raise Exception(f"Image not found: {image}")
            return False

    @classmethod
    def press_key(
        cls,
        key: str,
        delay: float = 0,
    ) -> None:

        pyautogui.press(key)
        time.sleep(delay)