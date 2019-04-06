#!/usr/bin/env python

import time
import logging
from bluetoothctl import Bluetoothctl

SLEEP_SECONDS = 5
YAMAHA_MAC = '00:A0:DE:04:07:17'


def main():
    logging.basicConfig(level=logging.DEBUG)

    ctl = Bluetoothctl()
    while True:
        time.sleep(SLEEP_SECONDS)
        if ctl.is_connected():
            continue

        ctl.power_on()
        ctl.connect(YAMAHA_MAC)


if __name__ == '__main__':
    main()
