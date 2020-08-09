class CarListing():

    def __init__(self, name:str, price:float, phone:str, location: str, mileage: int):

        self.name = name
        self.price = price
        self.phone = phone
        self.loaction = location,
        self.mileage = mileage

    def to_list(self):

        return [self.name, self.price, self.mileage, self.dealerPhone, self.dealerLoaction]

    def to_dictionary(self):

        return {"Name": self.name, "Price": self.price, "Milege": self.mileage, "Phone": Number }
