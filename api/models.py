from rest_framework import serializers
from django.db import models

# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(default=None, blank=True, null=True, max_length=50)
    email = models.CharField(default=None, blank=True, null=True, max_length=50)
    phone = models.CharField(default=None, blank=True, null=True, max_length=50)
    agenda_slug = models.CharField(default=None, blank=True, null=True, max_length=50)
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()