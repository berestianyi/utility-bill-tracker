from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect

from bills.forms import BillsForm
from bills.models import BillSubCategory
from buildings.forms import BuildingForm
from buildings.models import Building


def add_bill(request, building_key):
    building = Building.objects.get(pk=building_key)
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
        return render(request, 'bills/add_bill.html', {'form': form})


def add_input(request):
    if request.method == 'POST':
        return render(request, 'bills/include/htmx_add_bill_input.html')
    return HttpResponse("Invalid method", status=405)


def load_bill_category(request):
    category_id = request.GET.get("category")
    bills = BillSubCategory.objects.filter(bill_category=category_id)
    return render(request, "bills/include/bill_options.html", {'bills': bills})


def load_tariff_measure_unit(request):
    bill_name = request.GET.get("name")
    bill = BillSubCategory.objects.filter(pk=bill_name).first()
    return render(request, "bills/include/htmx_tariff_and_measure_unit.html", {'bill': bill})


def bill_inputs_sum(request):
    if request.method == 'POST':
        amount = request.POST.get("amount", 0)
        bill = request.POST.get("name")
        bill_name = BillSubCategory.objects.filter(pk=bill).first()
        result = Decimal(amount) * Decimal(bill_name.tariff)
        return render(request, "bills/include/dynamic_bill_inputs_sum.html", {'result': result})
    return HttpResponse(status=400)
