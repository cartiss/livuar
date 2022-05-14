from django import forms
from django.forms import TextInput

from reservation.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("customer_name", "customer_phone", "date", "time", "party_size")

        widgets = {
            "customer_name": TextInput(attrs={
                'placeholder': 'Your name',
            }),
            "customer_phone": TextInput(attrs={
                'placeholder': 'Your phone',
            }),
            "date": TextInput(attrs={
                'placeholder': '22-07-2006',
            }),
            "time": TextInput(attrs={
                'placeholder': '12:00',
            }),
            "party_size": TextInput(attrs={
                'placeholder': '1',
            }),
        }