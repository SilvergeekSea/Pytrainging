from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms/<int:id>', views.room_list,name="room_list"),
]