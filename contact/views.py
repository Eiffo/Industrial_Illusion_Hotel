from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Contact_Upload

def contact(request):
    if request.method == 'POST':
        form = Contact_Upload(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Wiadomość została pomyślnie wysłana!")
            return redirect('contact')
    else:
        form = Contact_Upload()

    return render(request, "contact/contact.html", {'form': form})
