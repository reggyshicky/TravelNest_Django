from django.shortcuts import render, redirect
from .models import Flight, Train, Airport, Passenger
from . forms import FlightForm, BookFlightForm
from django.db.models import F

# Create your views here.
def home(request):
    flights = Flight.objects.all()
    
    if request.method == "POST":
        form = FlightForm(request.POST) #instace
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = form
            return render(request, "accounts/index.html", {"form": form})
    else:
        form = FlightForm()
    context = {
        "flights" : flights,
        "form": form
        
    }
    return render(request, "accounts/index.html", context)




def flightdetails(request, pk):
    flight = Flight.objects.get(pk=pk)
    passengers_in_flight = flight.passengers.all()  
    all_passengers = Passenger.objects.all()
    psgNotInFlight = all_passengers.exclude(pk__in=passengers_in_flight.values_list('pk', flat=True)) #second pk, is pk for passenger instance.
    
    
    if request.method == "POST":
        form = BookFlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flightdetails", pk=flight.pk)
        else:
            return render(request, "accounts/flightdetails.html", {"form": form, "flight": flight})     
    else:
        form = BookFlightForm()

    context = {
        "flight": flight,
        "psgNotInFlight": psgNotInFlight,
        "form": form
    }

    return render(request, "accounts/flightdetails.html", context)

