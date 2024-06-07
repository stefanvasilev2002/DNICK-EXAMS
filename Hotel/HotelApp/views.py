from django.shortcuts import render, redirect
from .forms import HotelReservationForm
from .models import *


def index(request):
    qs = Room.objects.filter(is_cleaned=True, beds__lt=5)
    return render(request, 'index.html', context={'rooms': qs})


def contact_us(request):
    if request.method == 'POST':
        form_data = HotelReservationForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            reservation = form_data.save(commit=False)
            reservation.user = request.user
            reservation.image = form_data.cleaned_data['image']
            reservation.save()
            return redirect('/contact_us')
    return render(request, 'contact_us.html', context={'form': HotelReservationForm})


def room_details(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'room_details.html', context={'room': room})
