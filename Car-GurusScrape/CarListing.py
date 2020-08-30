class CarListing():

    def __init__(self, name: str, price: float, phone: str, location: str, mileage: int, listingUrl: str):

        self.name = name
        self.price = price
        self.phone = phone
        self.location = location
        self.mileage = mileage
        self.listingUrl = listingUrl

    def to_list(self):

        return [self.name, self.price, self.mileage, self.phone, self.location, self.listingUrl]

    def to_dictionary(self):

        return {"car_name": self.name, "price": self.price, "mileage": self.mileage, 
                "phone": self.phone, "location": self.location, "url": self.listingUrl}
