import pandas as pd

class DataPacker():

    def __init__(self):
        
        pass

    def initialize_dict(self, obj):

        dictionary = obj.to_dictionary()

        for key in dictionary.keys():
            dictionary[key] = []

        return dictionary
    
    def add_obj_to_dictionary(self, obj, dictionary):

        objDict = obj.to_dictionary()

        for key in dictionary.keys():
            dictionary[key].append(objDict[key])

    def objs_to_dataframe(self, objList: list):

        objDict = self.initialize_dict(objList[0])

        for obj in objList:
            self.add_obj_to_dictionary(obj, objDict)

        return pd.DataFrame(objDict)
