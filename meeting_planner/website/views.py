from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner, Silver!")

def date(request):
    return HttpResponse("This page was servered at in Australia " + str(datetime.now()))

def about(request):
    return HttpResponse("This page is about Silver himself")