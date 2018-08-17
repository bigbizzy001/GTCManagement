from django.contrib import admin

from .models import Contact, Flight, Hotel, Visa

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'email', 'description')
    list_filter = ('subject', 'email')
    search_fields = ('name', 'subject')


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'to', 'departing', 'departure_date', 'passengers', 'flight_type', 'cabin_class')
    list_filter = ('departing', 'flight_type', 'cabin_class')
    search_fields =('name', 'to', 'departing', 'passengers', 'flight_type', 'cabin_class')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city', 'possible_location', 'check_in_date', 'check_out_date', 'number_of_rooms',
                    'occupancy', 'hotel_category')
    list_filter = ('city', 'possible_location', 'hotel_category')
    search_fields = ('city', 'possible_location', 'hotel_category')

@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'middle_name', 'date_of_birth', 'phone_number', 'email')
    list_filter = ('surname', 'phone_number', 'email')
    search_fields = ('surname', 'first_name', 'middle_name')



