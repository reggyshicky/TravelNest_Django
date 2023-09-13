from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

class Airport(models.Model):
    name = models.CharField(max_length=50)
    airportCode = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} {self.airportCode}"
    
FLIGHT_STATUS =[
    ("Cancelled", "CANCELLED"),
    ("Delayed", "DELAYED"),
    ("On Time", "ON_TIME")
]   
class BaseModel(models.Model):
    
    arrivalTime = models.TimeField()
    departureTime = models.TimeField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places =2)
    status = models.CharField(choices=FLIGHT_STATUS, max_length=10, blank=True, null=True)
    class Meta:
        abstract=True   # no class called BaseModel will be creating in the database

    
class Flight(BaseModel):
    pointOfDeparture = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_time")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_destination")
     
    class Meta:
         ordering = ("pointOfDeparture",)
         
    def __str__(self):
        return f"{self.pointOfDeparture}, {self.destination}, {self.departureTime}, {self.arrivalTime}"
    
class Train(BaseModel):
    pointOfDeparture = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="Train_time")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="Train_destination")
    def __str__(self):
        return f"{self.duration}, {self.price} {self.status}"
    
class Passenger(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    