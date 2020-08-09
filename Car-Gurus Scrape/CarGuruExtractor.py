import requests
from bs4 import BeautifulSoup
from CarWebBrowser import CarBrowser
from CarGuruParser import CarGuruParser
from CarGuruUrl import CarGuruListingsUrl


class CarGuruExtractor():

    def __init__(self, zipCode: int, radius: int, carId: str, maxResults = None):

        self.crawlUrl = CarGuruListingsUrl(zipCode, radius, carId)
        self.browser = CarBrowser()
        basePage = self.browser.get_page_content(self.crawlUrl.return_url())
        numberOfPages = int(CarGuruParser.get_max_pages(basePage))

        if maxResults:
            self.maxResults = min(numberOfPages, maxResults)
        
        else:
            self.maxResults = numberOfPages


    def get_pages(self):

        results = []
        pages = [self.crawlUrl.increment_page() for url in range(2, self.maxResults)]

        for page in pages:

            soup = self.browser.get_page_content(page)
            results.extend(soup)

        
        return results


zipC = 98225
radius = 150
carId = 'd2397'
cgs = CarGuruExtractor(zipC, radius, carId)
soup = cgs.get_pages()

