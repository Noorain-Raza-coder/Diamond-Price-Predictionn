from dataclasses import dataclass
import os
from src.logger import logging
from src.exception import CustomException
import sys


from sklearn.linear_model import LinearRegression , Lasso , ElasticNet
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor

# from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score
from sklearn.model_selection import cross_val_score

from src.utils import save_obj




@dataclass
class ModelTrainerConfig:
    model_object_path = os.path.join("artifacts" , "model.pkl")


class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config =  ModelTrainerConfig()

    def initiate_model_training(self , x_train , x_test , y_train , y_test):
        try :

            logging.info("Model Trianing start.")
            ## models
            models = {"LinearRegression" : LinearRegression(),
                        "Lasso" : Lasso(),
                        "ElasticNet" : ElasticNet(),
                        #  "DTRegressor" : DecisionTreeRegressor(),
                        #  "RFRegressor" : RandomForestRegressor()
                        }


            ## find best model
            model_Scores = []
            for model in models:
                score = cross_val_score(models[model], X=x_train , y=y_train , cv=5,scoring='r2').mean()
                model_Scores.append((model,score))

                print(model ,"->" ,"R2_score : " , score)
                print("="*30 ,'\n')


            logging.info("Best model is evaluated")
            ## sorting model based on scores
            model_Scores.sort(key=lambda x:x[1])
            best_model_score = model_Scores[-1]
  
            ## best model
            best_model = models[best_model_score[0]]

            ## trainging the best model
            best_model.fit(x_train,y_train)

            logging.info("Saving best model.")
            ## save best model into pkl file
            save_obj(obj=best_model , file_path=self.model_trainer_config.model_object_path)

            logging.info("Model Training is done.")


        except Exception as e:
            logging.info("Error occured in model training.")
            raise CustomException(e,sys)