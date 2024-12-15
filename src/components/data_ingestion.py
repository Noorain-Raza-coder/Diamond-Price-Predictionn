import os
from dataclasses import dataclass
import pandas as pd
from src.logger import logging
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts' , 'train.csv')
    test_data_path = os.path.join('artifacts' , 'test.csv')
    raw_data_path = os.path.join('artifacts' , 'raw.csv')



class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def InitiateDataIngestion(self):

        try:
            df = pd.read_csv("notebooks/data/gemstone.csv")
            logging.info("Dataset is Read.")

            df.to_csv(self.ingestion_config.raw_data_path , index=False , header=True)

            logging.info("Splitting dataset into train and test.")
            train_data , test_data = train_test_split(df,  test_size = 0.30 , random_state = 42)

            train_data.to_csv(self.ingestion_config.train_data_path , index = False)
            test_data.to_csv(self.ingestion_config.test_data_path , index = False)

            logging.info("Data Ingestion is completed.")
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            logging.info("Error occured in Data Ingestion config.")
            # print(e)

         


# if __name__ == '__main__':
#     obj = DataIngestion()
#     train_path , test_path = obj.InitiateDataIngestion()
#     print(train_path , test_path)