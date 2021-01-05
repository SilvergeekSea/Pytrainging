Model, Template, View
Model, view, controller, MVC, MTV are the same. 

Template
- Generate HTML
- Call template from view
- Pass data from view to template

Create templates folder under app folder. 
Create another folder related to app under templates folder. 
Create a new HTML file called welcome.html.

the structure must be correct on templates.
then on views.py, you add
from django.shortcuts import render

and use 
return render(request, "website/welcome.html") # template name

{{variable}} is a template variable. it will be rendered. 
Then you can pass down this variable from views.py. 
It actually uses dictionary type which got key and value. 

meetings/<int:id>
expect integer, should pass from url eg: meetings/2

meetings = Meeting.objects.all() -> retrieve all Meeting objects. 
# Get object count
num_meetings = Meeting.objects.count()

# Get a specific object
Meeting = Meeting.objects.get(pk=5)

urlpatterns = [
    path('/example/<int:x>', my_view)
] 
# passing integer x to my_view as x

