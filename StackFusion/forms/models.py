from django.db import models


# Create your models here.
class FormModel(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    dateOfBirth = models.DateField(max_length=10)
