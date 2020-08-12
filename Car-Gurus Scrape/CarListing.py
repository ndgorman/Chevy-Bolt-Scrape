class CarListing():

    def __init__(self, name: str, price: float, phone: str, location: str, mileage: int, listingUrl: str):

        self.name = name
        self.price = price
        self.phone = phone
        self.location = location,
        self.mileage = mileage
        self.listingUrl = listingUrl

    def to_list(self):

        return [self.name, self.price, self.mileage, self.phone, self.location, self.listingUrl]

    def to_dictionary(self):

        return {"Name": self.name, "Price": self.price, "Milege": self.mileage, 
                "Phone": self.phone, "Location": self.location, "URL": self.listingUrl}
