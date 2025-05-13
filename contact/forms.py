from django.forms import ModelForm
from .models import Contact

class ContactUpload(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']