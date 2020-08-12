class CarGuruListingsUrl():

    def __init__(self, zipCode: int, radius: int, carId: str, startingPage: int = 1):

        baseUrl = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action'
        self.zipCode = zipCode
        self.distance = radius
        self.carId = carId
        self.current_page = startingPage

        zipUrl = f'?zip={zipCode}'
        distUrl = f'&distance={radius}'
        carUrl = f'&entitySelectingHelper.selectedEntity={carId}'
        configurableUrl = f'{zipUrl}&showNegotiable=true&sortDir=ASC&0{distUrl}&sortType=DEAL_SCORE{carUrl}'

        self.baseUrl = baseUrl + configurableUrl

    def increment_page(self):

        self.current_page += 1

        return self.return_url_of_current_page()

    def link_to_listing(self, listingId):

        return self.baseUrl + f'#listing={listingId}'

    def return_url_of_current_page(self):

        return self.baseUrl + f'#resultsPage={self.current_page}'