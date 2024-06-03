import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('/Users/shabi/Desktop/desk/Hesham/my_files/k_notes2023/my_codes_kvr/ml_aws_deploy/notebook/data/StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

# # reading the data deviding in train and validation data will be created 

# # getting data ---> getting it from databases

# import os
# import sys
# from src.exception import CustomException
# from src.logger import logging
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# # wheen we perform data ingestion there should be some inputs that will be required 


# # using a dataclass... we can define our class variable by ourselves... as opposed we use init
# @dataclass
# class DataIngestionConfig:
#     train_data_path:str = os.path.join('artifacts', 'train.csv')   # making artifact folder to store the output
#     test_data_path:str = os.path.join('artifacts', 'test.csv')
#     raw_data_path:str = os.path.join('artifacts', 'data.csv')
    
    
# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()  # once we call this 3 inputs will come from above... 
        
        
#     def initiate_data_ingestion(self):
#         # read data from database --> creat a mongo client in util.py and call it here
#         # we will move with normal method this time.
#         logging.info("Entered the data ingestion method/component")
#         try:
#             df = pd.read_csv('notebook/data/StudentsPerformance.csv')
#             logging.info("read the dataset as dataframe")
            
#             # creating the directories
#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
#             # if folder is there no need to create and if not then will make one
#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
#             logging.info("train test spit has been initiated")
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
#             train_set.to_csv(self.ingestion_config.train_data_path, index= False, header  = True)
#             test_set.to_csv(self.ingestion_config.test_data_path, index= False, header  = True)
            
            
#             logging.info("ingestion of the data is completed")
            
#             return (
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
                
#             )
            
#         except Exception as e:
#             raise CustomException(e, sys)
            
    
# if __name__ == "__main__":
#     obj = DataIngestion()
#     train_data, test_data = obj.initiate_data_ingestion()

