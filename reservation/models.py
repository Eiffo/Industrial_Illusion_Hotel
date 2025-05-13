from django.db import models

class Reservation(models.Model):
    name_surname = models.CharField(max_length=100)
    email = models.EmailField()
    arrival_date = models.DateField()
    departure_date = models.DateField()

    ROOM_CHOICES = [
        ("standard", "Standard room"),
        ("deluxe", "Deluxe room"),
        ("suite", "Apartment"),
        ("penthouse", "Penthouse"),
    ]
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    additional_wishes = models.TextField(blank=True)

class RoomCount(models.Model):
    room_type = models.CharField(max_length=20, unique=True, choices=Reservation.ROOM_CHOICES)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.room_type} ({self.quantity})"
