from . models import Flight, Airport
from django import forms

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            "arrivalTime",
            "departureTime",
            "price",
            "duration",
            "pointOfDeparture",
            "destination"    
        ]