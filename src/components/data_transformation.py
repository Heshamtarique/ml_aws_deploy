import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

# from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    
    
    
    
class DataTransformation:
    
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]   # numerical features
            
            # categorical features 
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            # sklearn pipeline -- numerical pipeline
            num_pipeline= Pipeline(                                    
                steps=[
                ("imputer",SimpleImputer(strategy="median")),   # imputing with median
                ("scaler",StandardScaler())

                ]
            )
            # categorical pipeline -- 
            cat_pipeline=Pipeline(
                # 3 steps below
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),    # categoricals imputed with most frequesnt -- mode
                ("one_hot_encoder",OneHotEncoder()),                    # encoding the categoricals
                ("scaler",StandardScaler(with_mean=False))              # scaling data
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
      