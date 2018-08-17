from django import forms
from .models import Contact, Flight, Hotel, Visa


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'subject', 'email', 'description')


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'phone', 'to', 'departing', 'departure_date', 'passengers', 'flight_type', 'cabin_class']
        widgets = {'departure_date': forms.DateInput()}


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name', 'phone', 'city', 'possible_location', 'check_in_date', 'check_out_date', 'number_of_rooms',
                    'occupancy', 'hotel_category')


class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['surname', 'first_name', 'middle_name', 'date_of_birth', 'phone_number', 'email']
        # widgets = {'phone_number': forms.DateTimeInput(attrs={'placeholder': 'Phone Number'})}
