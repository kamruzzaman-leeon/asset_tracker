# asset_tracker
Django app to track corporate assets such as phones, tablets, laptops  and other gears handed out to employees.
# Instruction 

## Table of Content

- [Installation](#installation)
- [Requirements](#requirements)
- [Test](#test)

## Installation
 0. make sure you have install the python in your system

 1. Clone the repository : 

        
        git clone https://github.com/kamruzzaman-leeon/asset_tracker.git
        

 2. Navigate to the project dicrectory:

          
        cd asset_tracker
        
 3. Create & activate the virtual environment
    - if(virtualenv):

            virtualenv env
            venv\Script\active
            
    - else
    
            pip install virtualenv
            virtualenv env
            venv\Script\active
      

## Requirements
- asgiref==3.7.2
- Django==4.2.4
- djangorestframework==3.14.0
- pytz==2023.3
- sqlparse==0.4.4
- tzdata==2023.3

### Install the require dependencies:
    pip install -r requirements.txt

### Database Setup:
    python manage.py makemigrations
    python manage.py migrate
   
### Running the Project:
    python manage.py runserver

### Initial Admin User:
    python manage.py createsuperuser

### Run Project:

1. Accessing the Django admin
    http://127.0.0.1:8000/admin/

- Log In:
    - Log In with Superuser Credentials
    - or Createsuperuser
- Manage Data:
    - Compaines
    - Employees
    - Devices
    - Device Logs
2. view all data:
    http://127.0.0.1:8000/api/

# TEST
    python manage.py test
