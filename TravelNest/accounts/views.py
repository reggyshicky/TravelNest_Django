from django.shortcuts import render
from .models import Flight, Train, Airport

# Create your views here.
def home(request):
    
    flights = Flight.objects.all()
    context = {
        "flights" : flights,
        
    }
    return render(request, "accounts/index.html", context)