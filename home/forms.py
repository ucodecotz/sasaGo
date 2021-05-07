from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Booking


class BookingForm(forms.Form):
    pickup_location = forms.CharField()
    destination = forms.CharField()
    booked_vehicle = forms.CharField()
    package_size = forms.CharField()
    phone = forms.CharField()
    
    class Meta:
        model = Booking
        fields = '__all__'



