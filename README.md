# GraphQL Test Project

## Instructions: 
  
### Docker:  
1. Clone the repo:  
    `git clone git@github.com:sf27/Django-GraphQL-Project.git`  
2. Build the docker image:  
    `cd Django-GraphQL-Project/ && docker-compose build`  
3. Starts the containers in the background and leaves them running:  
    `docker-compose up -d`  
4. Run the migrations:  
    `docker-compose run --rm django python manage.py migrate`  
5. Load test data:  
    `docker-compose run --rm django python manage.py loaddata ingredients`  
6. Create SuperUser (Optional):  
    `docker-compose run --rm django python manage.py createsuperuser`  
7. Open the following URL:  
    `http://127.0.0.1:8000/graphiql`  
    
### Without Docker:
1. Clone the repo:  
    `git clone git@github.com:sf27/Django-GraphQL-Project.git`  
2. Create a virtualenv and activate it:  
    `cd Django-GraphQL-Project && virtualenv -p python3 env && source env/bin/activate`  
3. Install the dependencies:  
    `pip install -r requirements.txt`  
4. Run the migrations:  
    `python manage.py migrate`  
5. Load test data:  
    `python manage.py loaddata ingredients`  
6. Create SuperUser (Optional):  
    `python manage.py createsuperuser` 
7. Run the development server:  
    `python manage.py runserver`  
8. Open the following URL:  
    `http://127.0.0.1:8000/graphiql`  