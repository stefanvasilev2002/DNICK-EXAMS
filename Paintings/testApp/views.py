from django.shortcuts import render, redirect
from .forms import ExhibitionForm
from .models import Exhibition, Painting


def index(request):
    exhibitions = Exhibition.objects.all()
    paintings = []
    for exhibition in exhibitions:
        for painting in Painting.objects.filter(exhibition=exhibition):
            paintings.append(painting)
            break
    return render(request, 'index.html', context={'exhibitions': exhibitions
                                                  , 'paintings': paintings})


def add_exhibition(request):
    if request.method == 'POST':
        form_data = ExhibitionForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return render(request, 'index.html', context={'exhibitions': Exhibition.objects.all()})

    return render(request, 'add_exhibition.html', context={'form': ExhibitionForm})

