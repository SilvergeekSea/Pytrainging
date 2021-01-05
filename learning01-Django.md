1. start a new venv
    py -m pip venv django_started
2. clone from github with requirement (create a new folder)
3. install requirement.txt
    py -m pip install -r requirement.txt
4. run "django-admin startproject meeting_planner" to start project
5. go to meeting_planner folder, run "python manage.py runserver"
6. Django created db.sqlite3 file automatically when we runserver. It contains  no data at this stage. 
7. It created 2nd meeting_planner folder which is core folder. 
8. settings.py is where project defined. 
9. urls.py - where we will put code that assigns urls to the page. 
10. asgi and wsgi is to deploy server to production. 
11. __init__.py is marking this folder as package. 

mainly foucs on settings.py and urls.py, which are created by Django admin. 

also db.sqlite3 and manage.py which are not created by Django admin but by running server. 




