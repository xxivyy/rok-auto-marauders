
import os
import time

import pyautogui
pyautogui.PAUSE = 0

class Automation:

    @staticmethod
    def move_to(
        start_x: int, 
        start_y: int,
        end_x: int,
        end_y: int,
        speed: int = 1,
        steps: int = 60,
    ) -> None:
        '''Move the mouse to a specific point on the screen with custom smoothing.'''

        wait_step = speed / steps
        for i in range(1, steps + 1):
            prog = i / steps # current progress 0-1
            prog = prog * prog * (3 - 2 * prog) # smoothstep easing -> slow start, fast middle, slow end

            # calculate relative position based on progress
            x = start_x + (end_x - start_x) * prog
            y = start_y + (end_y - start_y) * prog

            pyautogui.moveTo(x, y, duration=0)
            time.sleep(wait_step)

    @classmethod
    def click_image(
        cls,
        image: os.PathLike,
        confidence: float = 0.9,
        timeout: float = 0,
        speed: float = 0.5,
        delay: float = 0.2,
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

        start_x, start_y = pyautogui.position()

        cls.move_to(
            start_x=start_x,
            start_y=start_y,
            end_x=_image_center.x,
            end_y=_image_center.y,
            speed=speed,
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