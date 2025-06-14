from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Reservation, RoomCount
from re import match
from datetime import date

class ReservationUpload(ModelForm):
    class Meta:
        model = Reservation
        fields = ["name_surname", "email", "arrival_date", "departure_date", "room_type", "additional_wishes"]

    
    def clean_name_surname(self):
        name = self.cleaned_data["name_surname"]
        if not match(r"^[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+ [A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+$", name.strip()):
            raise ValidationError("Wprowadź poprawne imię i nazwiski, np. Jan Kowalski.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not match(r"[a-zA-Z0-9-_.]+@[a-z0-9-.]+.[a-z0-9]{1,6}", email.strip()):
            raise ValidationError("Niepoprawny email.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        room_type = cleaned_data.get("room_type")
        arrival = cleaned_data.get("arrival_date")
        departure = cleaned_data.get("departure_date")

        # check if room exists
        try:
            inventory = RoomCount.objects.get(room_type=room_type)
        except RoomCount.DoesNotExist:
            raise ValidationError("Nie można znaleźć informacji o dostępności pokoi.")

        # Count how many rooms is already booked between arrival and departure date
        overlapping_reservations = Reservation.objects.filter(
            room_type=room_type,
            arrival_date__lt=departure,
            departure_date__gt=arrival
        ).count()

        if overlapping_reservations >= inventory.quantity:
            # Find nearest date of free room
            next_available = (
                Reservation.objects
                .filter(room_type=room_type, departure_date__gte=arrival)
                .order_by("departure_date")
                .first()
            )
            next_available_date = next_available.departure_date if next_available else "nieznana"
            self.add_error("room_type", f"Brak dostępnych pokoi typu {room_type}. Najbliższy wolny termin to: {next_available_date}.")

        # check if date is valid
        if arrival and departure < date.today():
            self.add_error("arrival_date", "Data zameldowania nie może być wcześniejsza niż dzisiaj.")

        if arrival and departure and departure <= arrival:
            self.add_error("departure_date", "Data wymeldowania musi być późniejsza niż zameldowania.")
    
    def clean_additional_wishes(self):
        additional_wishes = self.cleaned_data["additional_wishes"]
        if len(additional_wishes) > 500:
            raise ValidationError("Za długa wiadomość.")
        return additional_wishes
