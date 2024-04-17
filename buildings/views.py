from django.shortcuts import render, redirect

from bills.forms import BillsForm
from bills.models import Bill
from buildings.forms import BuildingForm
from buildings.models import Building


def index(request):
    buildings = Building.objects.all()
    return render(request, 'buildings/index.html', {'buildings': buildings})


def add_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            new_building = form.save(commit=False)
            new_building.user = request.user
            new_building.save()
            form.save_m2m()
            return redirect('buildings:index')
    else:
        form = BuildingForm()
    return render(request, 'buildings/add_building.html', {'form': form})


def building_page(request, building_key):
    building = Building.objects.get(pk=building_key)
    bills = Bill.objects.all().filter(building=building_key)
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.building = building
            new_bill.save()
            return redirect('buildings:building', building_key)
        else:
            print("form is not valid")
    else:
        form = BillsForm()
    return render(request, 'buildings/building.html', {'building': building, 'form': form, 'bills': bills})