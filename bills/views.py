from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render

from bills.models import BillSubCategory


def add_input(request):
    if request.method == 'POST':
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


def bill_inputs_sum(request):
    if request.method == 'POST':
        amount = request.POST.get("amount", 0)
        tariff = request.POST.get("tariff", 0)
        result = Decimal(amount) * Decimal(tariff)
        return render(request, "bills/include/dynamic_bill_inputs_sum.html", {'result': result})
    return HttpResponse(status=400)
