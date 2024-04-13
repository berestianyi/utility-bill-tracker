from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from bills.forms import BuildingForm, BillsForm
from bills.models import Building, BillSubCategory, BillCategory, Bill


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


def add_bill(request, building_key):
    # building = Building.objects.get(pk=building_key)
    # if request.method == 'POST':
    #     form = BillsForm(request)
    #     if form.is_valid():
    #         new_bill = form.save(commit=False)
    #         new_bill.building = building
    #         new_bill.save()
    #         return redirect('bills:building')
    # else:
    #     form = BillsForm()
    return render(request, 'bills/building.html')


def building_page(request, building_key):
    building = Building.objects.get(pk=building_key)
    if request.method == 'POST':
        form = BillsForm(request, initial={'name': building.name})
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.building = building
            new_bill.save()
            return redirect('bills:building')
    else:
        form = BillsForm()
    return render(request, 'bills/building.html', {'building': building, 'form': form})


def add_input(request):
    if request.method == 'POST':
        # return HttpResponse('/bills/include/htmx_add_bill_input.html')
        return render(request, 'bills/include/htmx_add_bill_input.html')
    return HttpResponse("Invalid method", status=405)


def load_bill_category(request):
    category_id = request.GET.get("category")
    bills = BillSubCategory.objects.filter(bill_category=category_id)
    return render(request, "bills/include/bill_options.html", {'bills': bills})


def load_measure_unit(request):
    bill_name = request.GET.get("name")
    bill = BillSubCategory.objects.filter(pk=bill_name).first()
    return render(request, "bills/include/htmx_measure_unit.html", {'bill': bill})

