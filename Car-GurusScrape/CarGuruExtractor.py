import requests
from bs4 import BeautifulSoup
from CarWebBrowser import CarBrowser
from CarGuruParser import CarGuruParser
from CarGuruUrl import CarGuruListingsUrl


class CarGuruExtractor():

    def __init__(self, zipCode: int, radius: int, carId: str, maxResults = None):

        self.crawlUrl = CarGuruListingsUrl(zipCode, radius, carId)
        self.browser = CarBrowser()
        basePage = self.browser.get_page_content(self.crawlUrl.baseUrl)
        numberOfPages = int(CarGuruParser.get_max_pages(basePage))

        if maxResults:
            self.maxResults = min(numberOfPages, maxResults)
        
        else:
            self.maxResults = numberOfPages


    def get_pages(self):

        results = []
        
        for _ in range(0,self.maxResults):

            page = self.crawlUrl.return_url_of_current_page()
            soup = self.browser.get_page_content(page)
            listings = CarGuruParser.get_car_listings(soup)
            cars = [self.process_non_empty_listing(car) for car in listings]
            results.extend(cars)
            
            self.crawlUrl.increment_page()

        return [x for x in results if x]

    def process_non_empty_listing(self, listing):

        if len(list(listing)):
            return CarGuruParser.parse_listing_to_object(listing, self.crawlUrl)
        else:
            pass