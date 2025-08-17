from django.shortcuts import render
from django.shortcuts import Http404
from .room_data import ROOM_INFO
from django.utils.translation import gettext as _

def rooms(request):
    return render(request, "rooms/rooms.html")

def room_detail(request, room_type):
    room = ROOM_INFO
    if not room:
        raise Http404(_("Nie znaleziono takiego pokoju."))
    return render(request, "rooms/room_detail.html", {"room": room.get(room_type)})
