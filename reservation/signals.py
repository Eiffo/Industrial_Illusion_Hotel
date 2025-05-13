from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import RoomCount

@receiver(post_migrate)
def create_room_inventory(sender, **kwargs):
    default_rooms = {
        "standard": 4,
        "deluxe": 3,
        "suite": 2,
        "penthouse": 1,
    }

    for room_type, quantity in default_rooms.items():
        RoomCount.objects.get_or_create(room_type=room_type, defaults={"quantity": quantity})
