from django.contrib import admin
from .models import Reservation, RoomCount

class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name_surname", "arrival_date", "email", "room_type")

class RoomCountAdmin(admin.ModelAdmin):
    list_display = ("room_type", "quantity")

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(RoomCount, RoomCountAdmin)
