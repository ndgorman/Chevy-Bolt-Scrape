import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


class CarBrowser():

    def __init__(self):
        
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
       
    def get_page_content(self, url):
        
        self.driver.get(url)
        time.sleep(15)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        
        return soup

    def __del__(self):   
        
        self.driver.close()

    def close(self):

        self.close()