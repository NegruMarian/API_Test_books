from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    # chrome = webdriver.Chrome("D:\Marian\pers\chromeDriver")
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.set_page_load_timeout(10)
    chrome.maximize_window()
    chrome.get("https://simple-books-api.glitch.me")

    def close(self):
        self.chrome.quit()