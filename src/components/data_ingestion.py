import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from components.data_transformation import DataTransformation
from components.data_transformation import DataTransformationConfig
from components.model_trainer import ModelTrainer, ModelTrainerConfig
logging.info("started_process")
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifact", "train.csv")
    test_data_path: str=os.path.join("artifact", "test.csv")
    raw_data: str=os.path.join("artifact", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()

    def  initie_data_ingestion(self):
        logging.info("Data reading started")
        try:
            df =pd.read_csv("G:\\ML_project\\notebook\\data\\stud.csv")
            logging.info("read the dataset as detaframe")
            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path), exist_ok=True)
            df.to_csv(self.ingestionconfig.raw_data,index=False, header=True)
            logging.info("Train Test Split initiated")
            train_set, test_set=train_test_split(df, test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)
            logging.info("Ingessition of the data is completed")
            return(
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initie_data_ingestion()
    data_transformation=DataTransformation()
    train_arr, test_arr,_=data_transformation.initiate_data_transformation(train_data, test_data)
    model_trainer=ModelTrainer()
    model_trainer.initiate_model_traning(train_arr,test_arr)














