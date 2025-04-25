import os 
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd 
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    ## Note: Adding the different data transformation methods here.
    
    # I am just using the train_test_split method from sklearn to split the data into train and test sets.
    # In a real-world scenario, you would use more complex methods to transform the data.
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        
        # Splitting the data into train and test sets
        train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
    
        # Saving the train and test sets to csv files
        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Data transformation completed and train/test sets saved.")
        logger.info(f"Train set shape: {train_set.shape}")
        logger.info(f"Test set shape: {test_set.shape}")
        
        print(train_set.shape)
        print(test_set.shape)
        