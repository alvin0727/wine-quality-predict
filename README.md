# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/alvin0727/End-To-End-ML-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.10 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### Dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/alvin0727/End-To-End-ML-Project.mlflow \
MLFLOW_TRACKING_USERNAME = alvin0727 \
MLFLOW_TRACKING_PASSWORD = b9d019bd3526bf93e3920cc9bb1c502db1e8ff34 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/alvin0727/End-To-End-ML-Project.mlflow 

export MLFLOW_TRACKING_USERNAME=alvin0727 

export MLFLOW_TRACKING_PASSWORD=b9d019bd3526bf93e3920cc9bb1c502db1e8ff34

```

For windows:

```bash
$env:MLFLOW_TRACKING_URI = "https://dagshub.com/alvin0727/End-To-End-ML-Project.mlflow"

$env:MLFLOW_TRACKING_USERNAME = "alvin0727"

$env:MLFLOW_TRACKING_PASSWORD = "b9d019bd3526bf93e3920cc9bb1c502db1e8ff34"

```