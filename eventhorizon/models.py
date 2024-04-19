from django.db import models

class Trip(models.Model):
    city_name = models.CharField(max_length=100)
    package = models.IntegerField()
    duration = models.CharField(max_length=50)
    upcoming_trip_date = models.DateField()

    def __str__(self):
        return self.city_name


class SendToTrip(models.Model):
    destination = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    boarding = models.CharField(max_length=200)
    contactm = models.CharField(max_length=15)
    contacte = models.EmailField()

    def __str__(self):
        return self.name