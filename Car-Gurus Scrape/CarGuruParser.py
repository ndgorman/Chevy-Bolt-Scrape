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

        carName = soup.find("div", class_="_4BPaqe").h4.text
        carPrice = soup.find("div", class_="_4SFkcZ").text
        mileage = soup.find("div", class_="qUF2aQ").text
        dealLocale = soup.find("p" , class_="qUF2aQ").text
        phoneNumber = soup.find("button","_4wsjoT").find("div").text
        
        listingRef = soup.find("a", class_ ="JtRSix _5ef8K2")["href"]
        listingId = listingRef.split("=")[-1]

        url = urlObj.link_to_listing(listingId)

        return CarListing(carName, carPrice, phoneNumber, dealLocale, mileage, url)
