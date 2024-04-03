from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'bills/index.html')


def add_building(request):
    return render(request, 'bills/add_building.html')


def add_bill(request):
    pass


def building(request):
    pass


def add_input(request):
    if request.method == 'POST':
        # return HttpResponse('/bills/include/htmx_add_bill_input.html')
        return render(request, 'bills/include/htmx_add_bill_input.html')
    return HttpResponse("Invalid method", status=405)
