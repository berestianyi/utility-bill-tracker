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
    total = Bill.total_sum(building_key=building_key)
    return render(request, 'buildings/building.html', {
        'building': building,
        'bills': bills,
        'total_sum': total,
    })
