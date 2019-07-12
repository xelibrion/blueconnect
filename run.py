#!/usr/bin/env python

import time
import logging
from bluetoothctl import Bluetoothctl, pexpect

SLEEP_SECONDS = 5
YAMAHA_MAC = '00:A0:DE:04:07:17'


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")

    log = logging.getLogger()

    ctl = Bluetoothctl()
    while True:
        try:
            if ctl.is_connected():
                continue

            log.info('Device is not connected, attempting to connect')
            ctl.power_on()
            ctl.connect(YAMAHA_MAC)
            log.info('Device is now connected')
        except pexpect.exceptions.TIMEOUT:
            continue

        time.sleep(SLEEP_SECONDS)


if __name__ == '__main__':
    main()
