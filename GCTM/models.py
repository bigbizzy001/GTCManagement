from django.db import models

# Create your models here.
class Contact(models.Model):
    #TODO work on the placeholder field
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30) #work on the placeholder field
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Flight(models.Model):
    FLIGHT_PASSENGERS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                         ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'),
                         ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'))
    FLIGHT_TYPES = (('one way', 'One Way'), ('round trip', 'Round Trip'))
    CABIN = (('business', 'Business'), ('economy', 'Economy'), ('premium', 'Premium'), ('first', 'First'))

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)  # work on the placeholder field
    to = models.CharField(max_length=50)
    departing = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    passengers = models.CharField(choices=FLIGHT_PASSENGERS, default='1', max_length=30)
    flight_type = models.CharField(choices=FLIGHT_TYPES, default='one way', max_length=30)
    cabin_class = models.CharField(choices=CABIN, default='economy', max_length=30)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    ROOM_NUMBER = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                   ('9', '9'), ('10', '10'))
    ROOM_OCCUPANCY = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'))
    CATEGORY = (('first', 'First Class Hotel'), ('luxury', 'Luxury Hotel'), ('standard', 'Standard Hotel'),
                ('tourist', 'Tourist Hotel'))
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)  # work on the placeholder field
    city = models.CharField(max_length=30)
    possible_location = models.CharField(max_length=30)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    number_of_rooms = models.CharField(choices=ROOM_NUMBER, default='1', max_length=30)
    occupancy = models.CharField(choices=ROOM_OCCUPANCY, default='1', max_length=30)
    hotel_category = models.CharField(choices=CATEGORY, default='first', max_length=30)

    def __str__(self):
        return self.name


class Visa(models.Model):
    #VISA_TYPE =

    surname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    # visa_type =

    def __str__(self):
        return self.surname + " " + self.first_name



