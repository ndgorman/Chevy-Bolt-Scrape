import re
from CarListing import CarListing
from typing import List


class CarGuruCleaner():

    def __init__(self):

        pass

    def remove_non_numeric(self, word):

        return re.sub('[^0-9]', '', word)

    def is_incomplete_car(self, carListing: CarListing):

        return all(carListing.to_list())

    def listing_cleanse(self, listing:CarListing):

        listing.price = self.remove_non_numeric(listing.price)
        listing.mileage = self.remove_non_numeric(listing.mileage)
        listing.location = ''.join(listing.location.split(' ')[:2])

        return listing

    def process_listings(self, listingBlock: List[CarListing]) -> List[CarListing]:

        filteredListings = filter(self.is_incomplete_car, listingBlock)

        return [self.listing_cleanse(car) for car in filteredListings if car]
