URLs 
- Link building (automatically generate URLs)
- Named URL mapping

for loops in templates
# only shows code instead of html format
It's interesting that when I passed extra dictionary as parameters to welcome.html, it actually stop that page to be interpreted to html but showing entire code instead. 
correct code:
def welcome(request):
    return render(request, "website/welcome.html",
                {"meetings": Meeting.objects.all(),"rooms": Room.objects.all()}
                )

wrong code:
def welcome(request):
    return render(request, "website/welcome.html",
                {"meetings": Meeting.objects.all()},{"rooms": Room.objects.all()}
                )                

Everything started with urls.py and start with default welcome page. 
urls.py called welcome functions which is defined in the website.views                
in the website.views.py, it called database to retrieve all meetings and rooms objects and passed it to welcome.html.
Welcome.html used 2 for loops and listed all href links for each resource with id as parameters. 
Each resource called urls py name and passing down id to functions of views (for detailed page)
from meeting.views.py detail functions, it called template page to with new parameters (each object) and display details.

path can't have same string otherwise, they will point to the same. 


Creat a CSS stylesheet
CSS file is sent to browser and browser reach them. HTML define content while CSS define how to show it. 
create folder structure and style.css
use <link rel="stylesheet" href="/static/website/style.css"> to apply html
must stop Django and restart to see the effect. 

better format:
<link rel="stylesheet" href="{% static 'website/style.css' %}">

You can put image files under static and use
<img src="{% static 'website/calendar.jpg' %}" width="500px">

use template inheritence.
when use it, u can't have <img src="{% static 'website/calendar.jpg' %}" width="500px"> with in the html? with in the blockcontent? 
answer: you must include {% load static %} in the page which loads static. 