from django.shortcuts import render

def rooms(request):
    return render(request, "rooms/rooms.html")
