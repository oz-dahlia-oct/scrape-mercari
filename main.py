#!/usr/bin/env python
# coding: utf-8


# import built-in modules
import time
import os


# Import original modules
from mer import MERController
from mylogging import Log
from conf import Conf


if __name__ == '__main__':

    if not os.path.isdir('log'):
        os.mkdir('log')

    Log.start()

    c = MERController()
    c.goto_sell_page()
    time.sleep(3)

    while True:
        if c.driver.current_url == c.SELL_URL:
            c.fill_form()
            time.sleep(10)
            c.quit()
            break
        Log.printlog(
            "driver current url :",
            c.driver.current_url,
        )
        time.sleep(1)

    time.sleep(Conf.end_sleep)
    Log.print_length()
    Log.save_log()
    Log.end()

