# unused

import os
import sys

from selenium import webdriver

from robot.libraries.BuiltIn import BuiltIn


class BrowserSetup:
    def __init__(self):
        self.DOWNLOAD_DIR = os.path.abspath(
            os.path.normpath(
                os.path.join(os.path.dirname(__file__), "..", "data", "downloads")
            )
        )
        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)

    def _get_chrome_options(self, headless=False):
        # prefer selenium.webdriver from sys.modules to avoid cross-module mismatches
        webdriver_mod = sys.modules.get("selenium.webdriver", webdriver)
        options = webdriver_mod.ChromeOptions()
        options.add_argument("--incognito")
        if headless:
            options.add_argument("--headless")

        # stronger prefs to suppress dialogs and enable automatic downloads
        prefs = {"download.default_directory": self.DOWNLOAD_DIR}
        options.add_experimental_option("prefs", prefs)
        return options

    def _get_firefox_options(self, headless=False):
        webdriver_mod = sys.modules.get("selenium.webdriver", webdriver)
        options = webdriver_mod.FirefoxOptions()
        options.add_argument("--private-window")
        if headless:
            options.add_argument("--headless")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", self.DOWNLOAD_DIR)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/octet-stream,application/pdf,text/x-bibtex,application/x-bibtex",
        )
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("pdfjs.disabled", True)
        return options

    def _get_browser_options(self, browser="chrome", headless=False):
        if browser == "chrome":
            return self._get_chrome_options(headless)
        elif browser == "firefox":
            return self._get_firefox_options(headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}")


browser_setup = BrowserSetup
