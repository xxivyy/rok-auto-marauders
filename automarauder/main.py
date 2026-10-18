import random
import time

from .rok import ROK


def main() -> None:

    ## -- Setup -- ##

    ROK.start_automarauder()
    dispatch_timer = time.perf_counter()

    ROK.claim_system_rewards()
    mail_timer = time.perf_counter()
    mail_randomizer = random.randint(300, 420)  # 5-7 minutes

    ## -- Main Loop -- ##

    while True:
        time.sleep(1)
        ROK.attempt_reconnect()  # attempt to reconnect if needed

        # Check Dispatch Every 3 Seconds (Auto Marauder)

        if time.perf_counter() - dispatch_timer >= 3:
            ROK.start_automarauder()
            dispatch_timer = time.perf_counter()

        # Collect Mail every 5-7 Minutes

        if time.perf_counter() - mail_timer >= mail_randomizer:
            ROK.claim_system_rewards()
            mail_timer = time.perf_counter()
            mail_randomizer = random.randint(300, 420)
