from django.forms import ModelForm
from .models import Contact

class Contact_Upload(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']