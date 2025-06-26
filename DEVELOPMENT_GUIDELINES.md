DEVELOPMENT GUIDELINES
======================

GENERAL STRUCTURE
-----------------

*   Use **FastAPI** for serving the application.
    
*   Use **Strawberry GraphQL** for defining schema and handling queries/mutations.
    
*   Maintain all mock data (models, teams, experiments) in memory inside `models_db`, `teams_db`, and `experiments_db`.
    
*   Use **Poetry** for dependency management and virtual environments.
    

CODING STANDARDS
----------------

*   Follow PEP8 conventions.
    
*   Use type hints everywhere (`Optional`, `List`, `str`, etc.).
    
*   Keep GraphQL schema clean, avoid over-nesting unnecessary fields.
    
*   Separate pure logic (e.g., `parse_model`) from GraphQL definitions.
    

GRAPHQL DESIGN
--------------

*   Define Strawberry `@strawberry.type` classes for data types.
    
*   Use `@strawberry.input` for mutation inputs.
    
*   Always return typed results in queries/mutations.
    
*   Add nullable handling for fields like `team_id` or `experiment_id`.
    
*   DEVELOPMENT WORKFLOW
    --------------------
    
    1.  Create a new feature branch.
        
    2.  Make code changes and add test queries.
        
    3.  Test locally using:  
        `poetry run uvicorn main:app --reload`
        
    4.  Use GraphQL playground at:  
        `http://localhost:8000/graphql`
        
    5.  Submit Pull Request (if in team setup).
        
    
    ERROR HANDLING
    --------------
    
    *   Always check for missing or malformed input in mutations.
        
    *   Prefer raising meaningful GraphQL errors or returning null with context.
        
    *   Handle edge cases like empty metric lists or missing team info.
        
    
    EXTENDING THE APP
    -----------------
    
    *   Add mutation to update or delete models.
        
    *   Add real database (SQLAlchemy, Tortoise ORM, or similar).
        
    *   Add user authentication with OAuth/JWT.
        
    *   Validate input data using Strawberry/Pydantic.
        
    
    VERSION CONTROL
    ---------------
    
    *   Use Git. Commit often with clear messages.
        
    *   Ignore `.venv/`, `__pycache__/`, and `.mypy_cache/`.
        
    *   Track your `pyproject.toml` and `poetry.lock`.