from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationUpload

def reservation(request):
    if request.method == "POST":
        form = ReservationUpload(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rezerwacja została przyjęta!")
            return redirect("reservation")
        #else: print(form.errors)

    else:
        form = ReservationUpload()

    return render(request, "reservation/reservation.html", {"form": form})
