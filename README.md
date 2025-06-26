ML Model Registry - FastAPI + Strawberry GraphQL
================================================

This is a simple in-memory GraphQL API built using FastAPI and Strawberry to manage a Machine Learning Model Registry. It supports querying and mutations for models, teams, and experiments.

SETUP INSTRUCTIONS (USING POETRY):

1.  Install Poetry: https://python-poetry.org/docs/#installation
    
2.  Create a new project folder and navigate to it
    
3.  `mkdir ml-model-registry && cd ml-model-registry`
    
4.  Initialize Poetry project:  
    `poetry init --no-interaction`
    
5.  Add dependencies:  
    `poetry add fastapi uvicorn strawberry-graphql`
    
6.  Create a `main.py` file and paste the code.
    
7.  Start the server:  
    `poetry run uvicorn main:app --reload`
    

GraphQL Playground URL:  
[http://localhost:8000/graphql](http://localhost:8000/graphql)

query {
  models {
    id
    name
    version
    description
    framework
    metrics {
      name
      value
    }
    team {
      name
    }
    experiment {
      id
      startTime
    }
  }
}
Query a model by name:
query {
  model(name: "customer-churn-xgb") {
    id
    name
    description
    framework
    deploymentStatus
    metrics {
      name
      value
    }
    team {
      name
    }
    experiment {
      startTime
      hyperparameters {
        name
        value
      }
    }
  }
}

mutation {
  addModel(modelInput: {
    name: "new-model",
    version: "1.0.0",
    description: "Test model",
    deploymentStatus: "TRAINING",
    framework: "scikit-learn",
    teamId: 401,
    experimentId: 201,
    metrics: [
      { name: "accuracy", value: 0.85 }
    ]
  }) {
    id
    name
    version
    description
  }
}
NOTES:

This project stores data in-memory only.

To persist data, consider integrating a database like PostgreSQL or MongoDB.

Suitable for learning GraphQL API design with FastAPI and Strawberry.

