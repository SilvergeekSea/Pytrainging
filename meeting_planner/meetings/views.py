from django.shortcuts import render, get_object_or_404
from meetings.models import Meeting,Room 
# Create your views here.
def detail(request,id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request, "meetings/detail.html",{"meeting": meeting})

def room_list(request,id):
    room = get_object_or_404(Room,pk=id)
    return render(request, "meetings/room_list.html",
                {"room":room}
                )