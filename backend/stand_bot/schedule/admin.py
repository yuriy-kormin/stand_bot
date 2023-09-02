from django.contrib import admin
from .models import Venue, Event, Timeslot

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Timeslot)

