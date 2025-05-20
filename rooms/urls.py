from django.urls import path
from . import views

urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<slug:room_type>/", views.room_detail, name="room_detail")
]