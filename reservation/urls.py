from django.urls import path
from . import views

urlpatterns = [
    path("", views.reservation, name="reservation"),
    path("payment", views.payment, name="payment"),
]
