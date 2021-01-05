from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from meetings.models import Meeting,Room 

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                {"num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse("This page was servered at in Australia " + str(datetime.now()))

def about(request):
    return HttpResponse("This page is about Silver himself")