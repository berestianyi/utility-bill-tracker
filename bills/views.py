from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect

from bills.forms import BillsForm, UploadFileBillForm
from bills.models import BillType, Bill
from buildings.models import Building
import bills.utils as utils


def add_bill(request, building_slug):
    building = Building.objects.get(slug=building_slug)
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.building = building
            new_bill.save()
            return redirect('buildings:building', building_slug)
        else:
            print("form is not valid")
    else:
        form = BillsForm()
        return render(request, 'bills/add_bill.html', {'form': form})


def add_file_bill(request, building_slug):
    building = Building.objects.get(slug=building_slug)
    # bills = Bill.objects.filter(name__bill=)
    if request.method == 'POST':
        form = UploadFileBillForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['bill_file']
            text_from_pdf = utils.pdf_reader(uploaded_file)
            general_info_dict: dict = utils.general_bill_info(text_from_pdf)
            if utils.is_heat_bill(text_from_pdf):
                heat_total_price_dict: str = utils.heat_total_price(text_from_pdf)
            else:
                communal_services_dict: dict = utils.communal_services_extract(text_from_pdf)

            new_bill = form.save(commit=False)
            new_bill.building = building
            new_bill.name = new_bill.name
            return redirect('buildings:building', building_slug)
        else:
            print("form is not valid")
    else:
        form = BillsForm()
        return render(request, 'bills/add_bill.html', {'form': form})


def add_input(request):
    if request.method == 'POST':
        return render(request, 'bills/include/htmx_add_bill_input.html')
    return HttpResponse("Invalid method", status=405)


def load_tariff_measure_unit(request):
    bill_name = request.GET.get("name")
    bill = BillType.objects.filter(pk=bill_name).first()
    return render(request, "bills/include/htmx_tariff_and_measure_unit.html", {'bill': bill})


def bill_inputs_sum(request):
    if request.method == 'POST':
        amount = request.POST.get("amount", 0)
        bill = request.POST.get("name")
        bill_name = BillType.objects.filter(pk=bill).first()
        result = Decimal(amount) * Decimal(bill_name.tariff)
        return render(request, "bills/include/dynamic_bill_inputs_sum.html", {'result': result})
    return HttpResponse(status=400)
