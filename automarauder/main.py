
from .util import ROK
import time
import random

def main(args: list[str]) -> None:

    ## :: Setup :: ##
    
    if not ROK.isMarchOutside():
        ROK.start_automarauder()
    dispatch_timer = time.time()

    ROK.claim_system_rewards()
    mail_timer = time.time()
    mail_randomizer = random.randint(300, 420)
    
    ## :: Main Loop :: ##
    while True:
        time.sleep(1)

        ROK.attempt_reconnect() # attempt to reconnect if needed

        # Check Dispatch Every 3 Seconds (Auto Marauder)
        if abs(time.time() - dispatch_timer) >= 3:
            dispatch_timer = time.time()
            if not ROK.isMarchOutside():
                ROK.start_automarauder()

        # Collect Mail every 5-7 Minutes
        if abs(time.time() - mail_timer) >= mail_randomizer:
            mail_timer = time.time()
            mail_randomizer = random.randint(300, 420)
            ROK.claim_system_rewards()
            