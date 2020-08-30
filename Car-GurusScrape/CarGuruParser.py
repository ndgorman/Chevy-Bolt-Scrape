from bs4 import BeautifulSoup
from CarListing import CarListing
from CarGuruUrl import CarGuruListingsUrl


class CarGuruParser():

    @staticmethod
    def get_listings_block(soup: BeautifulSoup):

        return soup.find("div", class_ = "_5K96zi _3QziWR")

    @staticmethod
    def get_car_listings(soup: BeautifulSoup):

        return soup.find_all("div", class_ = "EUQoKn")

    @staticmethod
    def get_max_pages(soup: BeautifulSoup):

        span = soup.find("span", class_ = "_5kJMfL")
        pageNumber = span.text.split(" ")[-1]

        return pageNumber

    @staticmethod
    def parse_listing_to_object(soup: BeautifulSoup, urlObj: CarGuruListingsUrl):

        listingRef = soup.find("a", class_ ="JtRSix _5ef8K2")["href"]
        listingId = listingRef.split("=")[-1]
        url = urlObj.link_to_listing(listingId)
        
        carName = next(soup.find("div", class_="_4BPaqe").find('h4').stripped_strings)
        
        value_or_none = lambda x: x.text if x else None
        carPrice = value_or_none(soup.find("span", class_="_4SFkcZ"))
        mileage =  value_or_none(soup.find("p", class_="qUF2aQ"))
        dealLocale =  value_or_none(soup.find("div" , class_="_66MGoB"))
        phoneNumber =  value_or_none(soup.find("button","_4wsjoT").find("div"))

        return CarListing(carName, carPrice, phoneNumber, dealLocale, mileage, url)
