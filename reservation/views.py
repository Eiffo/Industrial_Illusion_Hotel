from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def reservation(request):
    template = loader.get_template("reservation/reservation.html")
    return HttpResponse(template.render())
