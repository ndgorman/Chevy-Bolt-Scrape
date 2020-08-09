from bs4 import BeautifulSoup
from CarListing import CarListing


class CarGuruParser():

    def __init__(self):

        pass

    @staticmethod
    def get_listings_block(soup: BeautifulSoup):

        return soup.find("div", class_ = "_5K96zi _3QziWR")

    @staticmethod
    def get_car_listings(soup: BeautifulSoup):

        return soup.find_all("div", class_ = "_4yP575 _2PDkfp")

    @staticmethod
    def get_max_pages(soup: BeautifulSoup):

        span = soup.find("span", class_ = "_5kJMfL")
        pageNumber = span.text.split(" ")[-1]

        return pageNumber

    @staticmethod
    def parse_listing_to_object(soup: BeautifulSoup):

        carName = soup.find("div", class_="_4BPaqe").h4.text
        carPrice = soup.find("div", class_="_4SFkcZ").text
        mileage = soup.find("div", class_="qUF2aQ").text
        dealLocale = soup.find("p" , class_="qUF2aQ").text
        phoneNumber = soup.find("button","_4wsjoT").find("div").text

        return CarListing(carName, carPrice, phoneNumber, dealLocale, mileage)
