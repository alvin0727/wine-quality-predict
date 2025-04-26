# End-to-end-Machine-Learning-Project-with-MLflow
![MLflow](https://img.shields.io/badge/MLflow-%23FF7F00.svg?style=for-the-badge&logo=mlflow&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A complete ML pipeline with experiment tracking, model management, and deployment.

[**REFERENCE**](https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow)

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



## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/alvin0727/End-To-End-ML-Project
cd End-To-End-ML-Project
```

### 2. Create and activate conda environment

```bash
conda create -n mlproj python=3.10 -y
conda activate mlproj
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

[Documentation](https://mlflow.org/docs/latest/index.html)

```python
# MLflow Configuration
MLFLOW_TRACKING_URI=https://dagshub.com/alvin0727/End-To-End-ML-Project.mlflow
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_token
```

```bash
python script.py
```

## 🚀 Running the Project

### Option 1: Local Development

```bash
# Run training pipeline
python main.py

# Start FastAPI server
python app.py
```

### Option 2: Docker

```bash
# Build
docker-compose build

# Create
docker-compose up -d 
```

### MLflow Tracking UI

```bash
mlflow ui --port 5000
```

### Pipeline Workflow

1. **Trigger**: Runs on push to `main` branch (ignoring documentation/config changes)
2. **Steps**:
   - Checks out the code
   - Verifies Docker/Docker Compose installation
   - Builds Docker images
   - Stops existing containers
   - Deploys new containers
   - Cleans up project-specific resources

3. [**GitHub Runners**](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)