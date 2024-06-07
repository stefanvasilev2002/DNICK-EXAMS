from django.shortcuts import render, redirect
from .models import Event, EventBand, Band
from .forms import EventForm


def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', context={'events': events})


def event(request):
    if request.method == 'POST':
        form_data = EventForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            bands = form_data.cleaned_data['bands']
            band_list = bands.split(',')

            event_object = form_data.save(commit=False)
            event_object.user = request.user
            event_object.image = form_data.cleaned_data['image']
            event_object.num_participants = len(band_list)
            event_object.save()

            for band in band_list:
                band = Band.objects.get(name=band)
                band.events_count = band.events_count + 1
                band.save()
                EventBand.objects.create(band=band, event=event_object)
            return redirect("/events/add")

    return render(request, "events.html", context={'form': EventForm})
