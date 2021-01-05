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

To create a Django app is to create a new folder which contains all python files. And enter to project folder level which is meeting_planner. 
python manage.py startapp website
It will creat new folder and generate some files. 
Remove all other py files except __init__.py and views.py. 
modify settings.py with in Installed_apps section to add website

add content into Views.py

every time user refresh the url, a new url request is made and a new view is generated. 


the path in urls.py if it is '', then it's default page of url. 

#Models:
Models is Python classes which mapped to database tables. 
Each object is a row in the table. 

Migration is a Python script to change the database. As models changes, the database struture need to change to match modified models. 
Keep db strcture in sync with code. 
Auto-generated (but not always, you may need to write your own migration script)
python manage.py startapp meetings
You use python manage.py showmigrations to see migrations. 
apply migrations
python manage.py migrate
if you have sqlite, you can run
python manage.py dbshell
When create a new class in the models.py, 
you create new attributes (like title, date) and they will be created by Django in __init__ and database.

call python manage.py makemigrations to record new class and attributes we have typied in models.py. It found our new meeting class and create a meeting table in the database. 

We can use python manage.py sqlmigrate meetings 0001

You don't need to type 0001_initial.py, just 0001 is enough. Run this command line, it will create a new table. 


You can use python manage.py migrate to apply all migrations. 
new table name is meetings_meeting. meetings is app name and meeting is class name. 


Admin interface allows you to cre3ate and edit model data. 
register model with admin site. 

to create superuser
python manage.py createsuperuser

# Phone1234

Django Models purpose is to save Python objects in a database. 

You can google django model fields to find out the fields

Migration workflow steps
1. Change model code
2. Generate migration script (check the code Django generated!)
    python manage.py makemigrations
3. Optional. Check whether migrations are done. 
    python manage.py showmigrations
4. run migrations 
    python manage.py migrate
5. You can create a super user to login to admin
6. user admin to add data if you configure admin.py correctly. 

## notice when you add new fields or attributes to existing table, the Django will ask you to fill up the attributes for existing records. It doesn't like empty value. 

In the meeting class, 
room = models.ForeignKey(Room, on_delete=models.CASCADE)

That means if room get deleted, all meetings related to the room will be deleted. 
To clean up, you need to remove all files (except __init__.py) under migrations. You also can remove database as well. 
You need to make sure Room class is above meeting class as meeting class requires to load Room class. 

we can run migration, it automatically create database file. 

When we delete database file, that means you have to recreate super user as well. 

We need to add room data first as its required. 

