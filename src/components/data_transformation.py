from dataclasses import dataclass
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.logger import logging
from src.exception import CustomException
import sys
import os

from src.utils import save_obj




@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join("artifacts","preprocessor.pkl")



class DataTrasformation:

    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):

        try :

            categorical_columns = ['cut', 'color','clarity']
            numeric_columns = ['carat', 'depth','table', 'x', 'y', 'z']

            cut_labels = ["Fair", "Good", "Ideal", "Very Good", "Premium"]
            color_labels = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_lables = ['I1' , 'SI1' , 'SI2' ,'VS1' , 'VS2' , 'VVS1', 'VVS2' , 'IF']


            ## numerical pipeline
            numerical_pipeline = Pipeline( steps = [('imputing', SimpleImputer(strategy='median')), 
                                                    ('Scaling' , StandardScaler())
                                                ] )

            ## categorical pipeline
            categorical_pipeline = Pipeline(steps = [('imputing' , SimpleImputer(strategy='most_frequent')),
                                        ('encoding' , OrdinalEncoder(categories= [cut_labels , color_labels , clarity_lables])),
                                        ('Scaling' , StandardScaler())
                                        ] )


            ## transform the features
            preprocessor = ColumnTransformer(
                                            [("numeric_pipeline" , numerical_pipeline , numeric_columns),
                                            ("categorical_pipeline" , categorical_pipeline , categorical_columns)])

            

            
            return preprocessor
        
        except Exception as e:
            logging.info("Error occured in data transformation object.")
            raise CustomException(e, sys)




    def initiate_data_Transformation(self , train_data_path , test_data_path):
        
        try:
            logging.info("Data Transformation is started.")
            train_Data = pd.read_csv(train_data_path)
            test_Data = pd.read_csv(test_data_path)

            logging.info("Train and Test data is read")
            logging.info(f"Training Dataset : \n{train_Data.head().to_string()}")
            logging.info(f"Testing Dataset : \n{test_Data.head().to_string()}")



            target_variable = 'price'
            drop_columns = ['id' , target_variable]

            ## splitting independent and target variable
            x_train = train_Data.drop(columns=drop_columns, axis=1)
            y_train = train_Data[target_variable]

            x_test = test_Data.drop(columns=drop_columns, axis=1)
            y_test = test_Data[target_variable]


            logging.info("Getting the preprocessor object")
            preprocessor = self.get_data_transformation_object()


            x_train = preprocessor.fit_transform(x_train)
            x_test = preprocessor.transform(x_test)

            ## save the preprocessor object now, as it is fitted and transform using data

            save_obj(obj = preprocessor , file_path = self.data_transformation_config.preprocessor_obj_path)


            logging.info("Data Transformation is done.")

            return (x_train , x_test , y_train , y_test)
        
        except Exception as e:
            logging.info("Error occured in initiating data transformation.")

            raise CustomException(e, sys)
        
        
    