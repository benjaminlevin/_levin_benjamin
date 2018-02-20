using: 
    Django
    SQLite
    + other specified requirements

only install required to run web app is Django v1.10 (see requirements.txt)
// pip install Django==1.10 
    // pip must be installed: https://pip.pypa.io/en/stable/installing/

once Django is installed, run app locally by running 'python manage.py runserver' in root directory
(application runs at localhost:8000)

application features are designed to meet basic requirements outlined in Job_Application_Std Dev_Python_Sqllite.txt (provided by Apex staff and serving as a supplement to this document)

localhost:8000/cleardb route is provided to clear all stored appointments for development + test

web application is in development mode for review

no validations specified in app requirements -- however, page will reload (without saving to db) if any form fields are left blank with appointment form submission



