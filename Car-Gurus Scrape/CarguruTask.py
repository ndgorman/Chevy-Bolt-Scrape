from CarGuruExtractor import CarGuruExtractor
import CarguruCarProcesor


def carguru_task(**kwargs):

    cars = CarGurusScraper(kwargs['zipCode'],kwargs['carId'], kwargs['radius']).get_pages()
    parse_data = None
    put_data_storage = None