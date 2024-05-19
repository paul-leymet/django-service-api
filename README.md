# django-service-api 

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)


### Build

1. Create a virtual environment: `python3 -m venv env`

2. Activate the virtual environment:  `source env/bin/activate`

3. Install dependencies:  `pip install -r requirements.txt`


### Run
   
1. Run:  `python manage.py runserver`


### Use
   
1. Go to [localhost:8000/graphql](http://localhost:8000/graphql)
   
2. Type your graphQL query:

    ```
    query {
        allIngredients {
            id
            name
        }
    }
    ```

