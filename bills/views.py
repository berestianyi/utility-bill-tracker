from django.shortcuts import render


def index(request):
    return render(request,'bills/index.html')

def add_bill(request):
    pass

def building(request):
    pass
