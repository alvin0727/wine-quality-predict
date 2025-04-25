import os
from mlProject import logger 
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            # Read data
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            validation_status = True

            # Validation the columns
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break  

            os.makedirs(os.path.dirname(self.config.STATUS_FILE),  exist_ok=True)

            # Write the validation
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e