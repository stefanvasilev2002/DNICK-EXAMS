from django.shortcuts import render, redirect
from .forms import RepairForm
from .models import Repair


def index(request):
    return render(request, "index.html")


def repairs(request):
    if request.method == "POST":
        form_data = RepairForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            repair = form_data.save(commit=False)
            repair.user = request.user
            repair.image = form_data.cleaned_data['image']
            repair.save()
            return redirect("/repairs")
    qs = Repair.objects.filter(user=request.user, car__type="sedan")
    return render(request, "repairs.html", context={'repairs': qs, 'form': RepairForm})


def edit_repair(request, id):
    repair_instance = Repair.objects.filter(id=id).get()
    if request.method == "POST":
        repair = RepairForm(request.POST, instance=repair_instance)
        if repair.is_valid():
            repair.save()
        return redirect("repairs")
    else:
        repair = RepairForm(instance=repair_instance)

    return render(request, "edit_repair.html", {"form": repair})


def delete_repair(request, id):
    repair_instance = Repair.objects.filter(id=id).get()
    if request.method == "POST":
        repair_instance.delete()
        return redirect("repairs")

    return render(request, "delete_repair.html")


def repair_details(request, id):
    return render(request, "repair_details.html", context={'repair': Repair.objects.get(id=id)})
