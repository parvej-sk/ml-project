from src.logger import logging
from src.exception import CustomException
import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig

from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_training import ModelTrainer

'''
if __name__=="__main__":
    logging.info("execution started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()


        ##Transform data
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)


        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
    
'''


class TrainingPipeline:
    def run_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

            # Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_transormation(train_data_path, test_data_path)

            # Model Training
            model_trainer = ModelTrainer()
            trained_model = model_trainer.initiate_model_trainer(train_arr, test_arr)
            #print(model_trainer.initiate_model_trainer(train_arr,test_arr))

        except Exception as e:
            raise CustomException(e, sys)
        
