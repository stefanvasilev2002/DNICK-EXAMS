from django.shortcuts import render, redirect
from .models import Flight
from .forms import FlightForm


def index(request):
    return render(request, 'index.html')


def flights(request):
    if request.method == 'POST':
        form_data = FlightForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            flight = form_data.save(commit=False)
            flight.user = request.user
            flight.image = form_data.cleaned_data['image']
            flight.save()
            return redirect("/flights")
    qs = Flight.objects.filter(user=request.user, airport_takeoff="Skopje")
    return render(request, 'flights.html', context={'flights': qs, 'form': FlightForm})


def edit_flight(request, id):
    flight_instance = Flight.objects.get(id=id)
    if request.method == 'POST':
        flight = FlightForm(request.POST, instance=flight_instance)
        if flight.is_valid():
            flight.save()
        return redirect('flights')
    else:
        flight = FlightForm(instance=flight_instance)
    return render(request, 'edit_flight.html', context={'form': flight})
