from src.exception import CustomException
from src.logger import logging
import sys
import os
from src.utils import load_obj
import pandas as pd





class PredictionPipeline:
    
    def __init__(self) -> None:
        pass

    def initiate_prediction_pipeline(self , features):
        
        try:
            logging.info("Loading objects")
            ## load objects
            preprocessor_obj_path = os.path.join("artifacts" , "preprocessor.pkl")
            model_obj_path = os.path.join("artifacts" , "model.pkl")

            preprocessor = load_obj(preprocessor_obj_path)
            model = load_obj(model_obj_path)

            logging.info("Applying transformation")
            ## apply transformation
            transformed_data = preprocessor.transform(features)

            
            logging.info("Making prediction")
            ## predict the result
            prediction = model.predict(transformed_data)

            logging.info("Prediction is Calculated and returned")

            return prediction



        except Exception as e:
            logging.info("Error Occured in prediciton pipeline.")
            raise CustomException(e , sys)




class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    
    
    def get_Data_as_dataFrame(self):
        try :
            logging.info("Creating custom data")
            data = {"carat" : [self.carat],
                "depth" : [self.depth],
                "table" : [self.table],
                "x" : [self.x],
                "y" : [self.y],
                "z" : [self.z],
                "cut" : [self.cut],
                "color" : [self.color],
                "clarity" : [self.clarity]}

            logging.info("Returning Dataframe")
            final_data = pd.DataFrame(data)

            return final_data

        except Exception as e:
            logging.info("Error ocurred in Custom data")
            raise CustomException(e , sys)