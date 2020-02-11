from django.db import models


class Phonebook(models.Model):
    phone_number = models.CharField(max_length=12)
    fullname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
