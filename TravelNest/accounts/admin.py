from django.contrib import admin
from .models import Flight, Airport, Train, Passenger
# Register your models here.

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Train)
admin.site.register(Passenger)