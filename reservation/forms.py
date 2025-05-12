from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Reservation
from re import match
from datetime import date

class Reservation_Upload(ModelForm):
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
            raise ValidationError("Wrong email.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        arrival = cleaned_data.get("arrival_date")
        departure = cleaned_data.get("departure_date")

        if arrival and departure < date.today():
            self.add_error("arrival_date", "Data zameldowania nie może być wcześniejsza niż dzisiaj.")

        if arrival and departure and departure <= arrival:
            self.add_error("departure_date", "Data wymeldowania musi być późniejsza niż zameldowania.")
    
    def clean_additional_wishes(self):
        additional_wishes = self.cleaned_data["additional_wishes"]
        if len(additional_wishes) > 500:
            raise ValidationError("To long message.")
        return additional_wishes
