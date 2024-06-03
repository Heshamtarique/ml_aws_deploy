
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
from src.utils import save_object

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
      
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math score"
            numerical_columns = ["writing score", "reading score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            '''
            no.c_ and np.r_   concatanating with diff axis
            import numpy as np
            a = np.array([[1, 2, 3],
                        [11,22,33]]
                        )
            b = np.array([[4, 5, 6],
                        [44,55,66]]
                        )
            np.r_[a,b]
            >>> array([[ 1, 2,  3],
                    [11, 22, 33],
                    [ 4, 5,  6],
                    [44, 55, 66]])       
            >>> array([[ 1, 2, 3, 4, 5, 6],
           [11, 22, 33, 44, 55, 66]])     
                        
                        '''
                        
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            # save_object is defined in utils from where we called it here
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
