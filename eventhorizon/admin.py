from django.contrib import admin
from eventhorizon.models import Trip,SendToTrip

admin.site.register(Trip)
admin.site.register(SendToTrip)
