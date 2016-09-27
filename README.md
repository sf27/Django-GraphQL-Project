# GraphQL Test Project

## Instructions: 
  
### Docker:  
1. Clone the repo:  
    `git clone git@github.com:sf27/Django-GraphQL-Project.git`  
2. Build the docker image:  
    `cd Django-GraphQL-Project/ && docker-compose build`  
3. Starts the containers in the background and leaves them running:  
    `docker-compose up -d`  
4- Create migrations (Optional):  
    `docker-compose run --rm django python manage.py migrate`  
5- Create SuperUser (Optional):  
    `docker-compose run --rm django python manage.py createsuperuser`  
6- Load test data (Optional):  
    `docker-compose run --rm django python manage.py loaddata ingredients`  
4. Open the following URL:  
    `http://127.0.0.1:8000/graphiql`  
    
### Without Docker:
1. Clone the repo:  
    `git clone git@github.com:sf27/Django-GraphQL-Project.git`  
2. Create a virtualenv and activate it:  
    `cd Django-GraphQL-Project && virtualenv -p python3 env && source env/bin/activate`  
2. Install the dependencies:  
    `pip install -r requirements.txt`  
3. Run the migrations:  
    `python manage.py migrate`  
4. Run the development server:  
    `python manage.py runserver`  
5. Open the following URL:  
    `http://127.0.0.1:8000/graphiql`  