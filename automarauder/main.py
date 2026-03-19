
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
    mail_randomizer = random.randint(420, 600)
    
    ## :: Main Loop :: ##
    while True:
        time.sleep(1)

        # Check Dispatch Every 3 Seconds (Auto Marauder)
        if abs(time.time() - dispatch_timer) >= 3:
            dispatch_timer = time.time()
            if not ROK.isMarchOutside():
                ROK.start_automarauder()

        # Collect Mail every 7-10 Minutes
        if abs(time.time() - mail_timer) >= mail_randomizer:

            # Temp: Attempt Exiting Potential Popups (change later to only trigger on actual detection)
            ROK.exitPopups()

            mail_timer = time.time()
            mail_randomizer = random.randint(420, 600)
            ROK.claim_system_rewards()
            