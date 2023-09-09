from django.db import models

# Create your models here.
class BaseModel(models.Model):
    destination = models.CharField(max_length=150)
    arrivalTime = models.DateTimeField(auto_now_add=True)
    departureTime = models.DateTimeField(auto_now_add=True)
    origin = models.CharField(max_length=150)
    
    class Meta:
        abstract=True
        
class Flight(BaseModel):
    
    
    def __str__():
        return ""
    
    