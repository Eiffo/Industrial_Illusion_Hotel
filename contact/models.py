from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    message = models.TextField()
