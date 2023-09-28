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
        passenger_pk = request.POST["passenger_name"]
        passenger = Passenger.objects.get(pk=passenger_pk)
        print(passenger)
        flight.passengers.add(passenger)
        
        return redirect("flightdetails", pk)
    context = {
        "flight": flight,
        "psgNotInFlight": psgNotInFlight,
        "passengers_in_flight": passengers_in_flight,
    }

    return render(request, "accounts/flightdetails.html", context)

