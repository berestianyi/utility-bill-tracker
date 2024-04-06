from django.http import HttpResponse
from django.shortcuts import render, redirect

from bills.forms import BuildingForm
from bills.models import Building, BillSubCategory


def index(request):
    buildings = Building.objects.all()
    return render(request, 'bills/index.html', {'buildings': buildings})


def add_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            new_building = form.save(commit=False)
            new_building.user = request.user
            new_building.save()
            form.save_m2m()
            return redirect('bills:buildings')
    else:
        form = BuildingForm()

    return render(request, 'bills/add_building.html', {'form': form})


def add_bill(request):
    pass


def building_page(request):
    pass


def add_input(request):
    if request.method == 'POST':
        # return HttpResponse('/bills/include/htmx_add_bill_input.html')
        return render(request, 'bills/include/htmx_add_bill_input.html')
    return HttpResponse("Invalid method", status=405)
