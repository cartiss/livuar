from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Reservation(models.Model):
    customer_name = models.CharField(max_length=64)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    customer_phone = PhoneNumberField()