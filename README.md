# Hospital Management System

Hospital Management System based on Django web framework.
Respective platforms for Doctor, Patients, and HR Manager.
Appointments and prescription management available.

## Steps to install and run in local system:-

- Create a virtual environment
    ```python3 -m venv <env_name>```
    
- Activate virtual environment
    ```source <env_name>/bin/activate```
    
- Install requirements in venv
    ```pip install -r requirements.txt```
    
- Make migrations
    ```python manage.py makemigrations```
    
- Apply migrations
    ```python manage.py migrate``` 
    
- Create a super user
    ```python manage.py createsuperuser``` 
    
- Run the server
    ```python manage.py runserver``` 
    
\* <small>You can delete db.sqlite3 and then make your own migrations further.</small>                  