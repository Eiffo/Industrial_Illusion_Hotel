from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactUpload
from django.utils.translation import gettext as _

def contact(request):
    if request.method == 'POST':
        form = ContactUpload(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, _("Wiadomość została pomyślnie wysłana!"))
            return redirect('contact')
    else:
        form = ContactUpload()

    return render(request, "contact/contact.html", {'form': form})
