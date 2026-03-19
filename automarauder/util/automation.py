
import os
import pyautogui

class Automation:

    @classmethod
    def click_image(
        cls,
        image: os.PathLike,
        confidence: float = 0.9,
        timeout: float = 0,
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
        
        _image_center = pyautogui.center((_image.left, _image.top, _image.width, _image.height))
        pyautogui.moveTo(
            x=_image_center.x,
            y=_image_center.y,
            duration=delay,
            # optional: custom tween
        )

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