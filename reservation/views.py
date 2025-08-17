from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationUpload
from django.utils.translation import gettext as _

def reservation(request):
    if request.method == "POST":
        form = ReservationUpload(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Save data
            request.session["name_surname"] = data["name_surname"]
            request.session["email"] = data["email"]
            request.session["arrival_date"] = data["arrival_date"].strftime("%Y-%m-%d")
            request.session["departure_date"] = data["departure_date"].strftime("%Y-%m-%d")
            request.session["room_type"] = data["room_type"]
            request.session["additional_wishes"] = data.get("additional_wishes", "")

            return redirect("payment")
        #else: print(form.errors)

    else:
        form = ReservationUpload()

    return render(request, "reservation/reservation.html", {"form": form})

def payment(request):
    context = {
        "name_surname": request.session.get("name_surname"),
        "email": request.session.get("email"),
        "arrival_date": request.session.get("arrival_date"),
        "departure_date": request.session.get("departure_date"),
        "room_type": request.session.get("room_type"),
        "additional_wishes": request.session.get("additional_wishes"),
    }
    required_fields = ["name_surname", "email", "arrival_date", "departure_date", "room_type"]

    # Check if data exist
    if not all(context.get(field) for field in required_fields):
        messages.error(request, _("Brakuje danych rezerwacji. Wypełnij formularz."))
        return redirect("reservation")

    return render(request, "reservation/payment.html", context)