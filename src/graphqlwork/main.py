
# ===================================================================
# MOCK DATABASE
# This is a more realistic dataset with multiple interconnected entities.
# ===================================================================
# --- Teams ---
# The teams responsible for developing the models.

from fastapi import FastAPI
import strawberry
from typing import Optional,List
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
teams_db = [
 {"id": 401, "name": "Alpha Core ML"},
 {"id": 402, "name": "Risk & Fraud Analytics"},
 {"id": 403, "name": "Growth Hacking Squad"},
]
# --- Experiments ---
# The ML experiments that produced the models.
experiments_db = [
 {
 "id": 201,
 "startTime": "2023-08-10T09:00:00Z",
 "endTime": "2023-08-10T17:30:00Z",
 "hyperparameters": [
 {"name": "learning_rate", "value": "0.001"},
 {"name": "epochs", "value": "25"},
 {"name": "optimizer", "value": "Adam"},
 ],
 },
 {
 "id": 202,
 "startTime": "2023-09-01T11:00:00Z",
 "endTime": "2023-09-02T15:00:00Z",
 "hyperparameters": [
 {"name": "n_estimators", "value": "200"},
 {"name": "max_depth", "value": "10"},
 {"name": "eta", "value": "0.1"},
 ],
 },
 {
 "id": 203,

 "startTime": "2023-09-15T10:00:00Z",
 "endTime": "2023-09-15T10:45:00Z",
 "hyperparameters": [
 {"name": "C", "value": "1.0"},
 {"name": "kernel", "value": "rbf"},
 {"name": "gamma", "value": "scale"},
 ],
 },
 {
 "id": 204, # An experiment that has not yet resulted in a model
 "startTime": "2023-10-28T14:00:00Z",
 "endTime": None,
 "hyperparameters": [
 {"name": "dropout", "value": "0.3"},
 {"name": "embedding_dim", "value": "128"},
 ],
 },
]
# --- Models ---
# The central model registry.
models_db = [
 {
 "id": 1,
 "name": "image-classifier-resnet",
 "version": "2.1.0",
 "description": "State-of-the-art image classifier based on ResNet",
 "deploymentStatus": "PRODUCTION",
 "framework": "PyTorch",
 "metrics": [
 {"name": "accuracy", "value": 0.98},
 {"name": "top_5_accuracy", "value": 0.99},
 {"name": "latency_ms", "value": 50},
 ],
 "experiment_id": 201,
 "team_id": 401,
 },
 {
 "id": 2,
 "name": "customer-churn-xgb",
 "version": "1.4.2",
 "description": "Predicts customer churn using a high-performance",
 "deploymentStatus": "PRODUCTION",
 "framework": "XGBoost",

 "metrics": [
 {"name": "roc_auc", "value": 0.91},
 {"name": "f1_score", "value": 0.88},
 {"name": "precision", "value": 0.90},
 ],
 "experiment_id": 202,
 "team_id": 402,
 },
 {
 "id": 3,
 "name": "fraud-detection-svm",
 "version": "0.9.0",
 "description": "Legacy fraud detection model. Slated for replacem",
 "deploymentStatus": "ARCHIVED",
 "framework": "scikit-learn",
 "metrics": [{"name": "recall", "value": 0.85}],
 "experiment_id": 203,
 "team_id": 402,
 },
 {
 "id": 4,
 "name": "nlp-sentiment-bert",
 "version": "0.5.0",
 "description": "New BERT-based model for sentiment analysis of cu",
 "deploymentStatus": "STAGING",
 "framework": "TensorFlow",
 "metrics": [], # Still in staging, no final metrics yet
 "experiment_id": None, # In staging, not linked to a final experi
 "team_id": 401,
 },
 {
 "id": 5,
 "name": "ab-test-uplift-v1",
 "version": "1.0.0",
 "description": "Model to predict marketing uplift for A/B testing",
 "deploymentStatus": "TRAINING",
 "framework": "scikit-learn",
 "metrics": [],
 "experiment_id": None,
 "team_id": 403,
 },
 {
 "id": 6,
 "name": "legacy-recommender",
 "version": "1.0.0",
 "description": "Old recommender system. No metadata available.",
 "deploymentStatus": "ARCHIVED",
 "framework": "Unknown",
 "metrics": [],
 "experiment_id": None,
 "team_id": None, # Edge case: team has been dissolved
 },
]

@strawberry.type
class Metric:
    name:str
    value:float

@strawberry.type
class Hyperparameter:
    name:str
    value:str

@strawberry.type
class Team:
    id: int
    name: str

@strawberry.type
class Experiment:
    id: int
    startTime: str
    endTime: Optional[str]
    hyperparameters: List[Hyperparameter]


@strawberry.type
class Model:
    id: int
    name: str
    version: str
    description: str
    deploymentStatus: str
    framework: str
    metrics: List[Metric]
    team_id: Optional[int]
    experiment_id: Optional[int]


    @strawberry.field
    def team(self) -> Optional[Team]:
        for t in teams_db:
            if t["id"] == self.team_id:
                return Team(**t)
        return None
    @strawberry.field
    def experiment(self)->Optional[Experiment]:
        for e in experiments_db:
            if e["id"]==self.experiment_id:
                return Experiment(**e)
        return None
    
    
def parse_model(m: dict) -> Model:
    metrics = [Metric(**metric) for metric in m["metrics"]]

    return Model(
        id=m["id"],
        name=m["name"],
        version=m["version"],
        description=m["description"],
        deploymentStatus=m["deploymentStatus"],
        framework=m["framework"],
        metrics=metrics,
        team_id=m["team_id"],
        experiment_id=m["experiment_id"]
    )




@strawberry.type
class Query:
    @strawberry.field
    def models(self) -> List[Model]:
        return [parse_model(m) for m in models_db]

    @strawberry.field
    def model(self, name: str) -> Optional[Model]:
        for m in models_db:
            if m["name"] == name:
                return parse_model(m)
        return None

@strawberry.input
class MetricInput:
    name: str
    value: float

@strawberry.input
class ModelInput:
    name: str
    version: str
    description: str
    deploymentStatus: str
    framework: str
    teamId: Optional[int]
    experimentId: Optional[int]
    metrics: List[MetricInput]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_model(self,model_input:ModelInput)->Model:
        new_id=len(models_db)
        model_data = {
            "id": new_id,
            "name": model_input.name,
            "version": model_input.version,
            "description": model_input.description,
            "deploymentStatus": model_input.deploymentStatus,
            "framework": model_input.framework,
            "team_id": model_input.teamId,
            "experiment_id": model_input.experimentId,
            "metrics": [{"name": m.name, "value": m.value} for m in model_input.metrics]
        }

       
        models_db.append(model_data)

        
        return parse_model(model_data)

    
schema = strawberry.Schema(query=Query,mutation=Mutation)
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")





