**DEVELOPMENT GUIDELINES**

1.  **Project Setup (Using Poetry with src layout)**
    
    *   Create a new project with standard `src/` structure:  
        `poetry new your-project-name --src`
        
    *   Navigate into the project folder:  
        `cd your-project-name`
        
    *   Activate the virtual environment:  
        `poetry shell`
        
2.  **Install Dependencies**
    
    *   Add core libraries:  
        `poetry add fastapi uvicorn strawberry-graphql`
    VERSION CONTROL
    ---------------
    
    *   Use Git. Commit often with clear messages.
        
    *   Ignore `.env/`, `__pycache__/`, and `.mypy_cache/`.
        
    *   Track your `pyproject.toml` and `poetry.lock`.


**Creating the GraphQL API**

*   Inside `main.py`, set up FastAPI with Strawberry:

Run the App

  

Use Uvicorn to run the development server:

uvicorn your\_project\_name.main:app --reload