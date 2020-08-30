import pandas as pd
from CarGuruExtractor import CarGuruExtractor
from CarGuruCleaner import CarGuruCleaner
from DataPacker import DataPacker

def carguru_task(**kwargs):

    carListingObjs = CarGuruExtractor(kwargs['zipCode'], kwargs['radius'], kwargs['carId']).get_pages()
    cleaned_objs = CarGuruCleaner().process_listings(carListingObjs)
    packed_data = DataPacker().objs_to_dataframe(cleaned_objs)
    packed_data['source'] = 'Cargurus'
    packed_data.to_gbq(project_id=kwargs['projectId'], destination_table=kwargs['destinationTable'], if_exists= 'append')


