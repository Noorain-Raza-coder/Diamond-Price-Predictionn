from src.components import data_ingestion
from src.components.data_transformation import DataTrasformation
from src.exception import CustomException
import sys
import pandas as pd

from src.components.model_trainer import ModelTrainer


if __name__ == '__main__':

    try :

        ## trigerring data ingestion
        obj = data_ingestion.DataIngestion()
        train_path , test_path = obj.InitiateDataIngestion()
        print(train_path , test_path)

        ## data transformation
        data_trns_obj = DataTrasformation()
        x_train , x_test , y_train , y_test = data_trns_obj.initiate_data_Transformation(train_data_path=train_path ,test_data_path=test_path )

        # x_train = pd.DataFrame(x_train)
        # x_test = pd.DataFrame(x_test)

        ## printing top two rows
        print(x_train[:2])
        print(x_test[:2])
        print(y_train[:2])
        print(y_test[:2])

        print("\nModel training start :...")
        model_obj = ModelTrainer()
        model_obj.initiate_model_training(x_train = x_train , x_test = x_test , y_train = y_train , y_test = y_test)

        print("model training done.")


    except Exception as e:
        raise CustomException(e,sys)


