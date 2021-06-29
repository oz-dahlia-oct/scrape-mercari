#!/usr/bin/env python
# coding: utf-8


# import built-in modules
import time


# Import original modules
from conf import Conf
from mylogging import Log


# Import external packages
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if Conf.dist:
    pass
else:
    import chromedriver_binary



class Controller:
    """
    ログイン、操作するクラス
    """
    DRIVER_PATH = Conf.driver_path

    def __init__(
        self,
        download_dir='D:\\',
        headless=False,
        page_load_timeout=1000,
        window_size=['1500', '3000']
    ):
        """
        ・driver のセットアップ
        download_dir ：ファイルダウンロード時のダウンロード先
        headless ：Chrome driver の非表示モード
        """

        self.download_dir = download_dir
        self.options = webdriver.chrome.options.Options()
        self.options.add_argument('--no-sandbox') 
        if headless:
            self.options.add_argument('--headless')
        if download_dir!='':
            self.options.add_experimental_option("prefs", {"download.default_directory": download_dir})
        self.options.add_argument('--kiosk-printing')

        if Conf.dist:
            self.driver = webdriver.Chrome(self.DRIVER_PATH, options=self.options)
        else:
            self.driver = webdriver.Chrome(options=self.options)

        self.driver.command_executor._commands["send_command"] = (
           "POST",
           '/session/$sessionId/chromium/send_command'
        )
        params = {
           'cmd': 'Page.setDownloadBehavior',
           'params': {
               'behavior': 'allow',
               'downloadPath': download_dir
           }
        }
        self.driver.execute("send_command", params=params)
        self.driver.set_page_load_timeout(page_load_timeout)
        self.driver.set_window_size(*window_size)
        Log.printlog('controller is initialized')





class MERController(Controller):
    
    SELL_URL = "https://www.mercari.com/jp/sell/"

    def goto_sell_page(self):
        Log.printlog('going to sell page...')
        self.driver.get(self.SELL_URL)

    def fill_form(self):
        Log.printlog('filling form...')
        pass

    def _is_validated(self):
        lst = self.driver.page_source.split('ログアウト')
        return True if len(lst) >= 2 else False


    def is_validated(self, retries=5, wait=1):

        if self._is_validated():
            return True

        time.sleep(0.5)

        for i in range(retries):
            if self._is_validated():
                return True
            Log.printlog(
                'retrying validation', 
                i+1,
            )
            time.sleep(wait)

        return False


    def quit(self):
        """
        Chrome Driver を閉じる
        """
        self.driver.quit()
        Log.printlog()
        Log.printlog('quit controller')
        Log.printlog()

