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
    user_data_2020 = [
        {"label": "JAN", "y": 58200},
        {"label": "FEB", "y": 59110},
        {"label": "MAR", "y": 60320},
        {"label": "APR", "y": 61440},
        {"label": "MAY", "y": 62580},
        {"label": "JUN", "y": 63190},
        {"label": "JUL", "y": 64000},
        {"label": "AUG", "y": 64290},
        {"label": "SEP", "y": 65530},
        {"label": "OCT", "y": 65300},
        {"label": "NOV", "y": 65340},
        {"label": "DEC", "y": 64530}
    ]
    user_data_2021 = [
        {"label": "JAN", "y": 65100},
        {"label": "FEB", "y": 66210},
        {"label": "MAR", "y": 66540},
        {"label": "APR", "y": 66680},
        {"label": "MAY", "y": 67500},
        {"label": "JUN", "y": 68850},
        {"label": "JUL", "y": 69000},
        {"label": "AUG", "y": 70130},
        {"label": "SEP", "y": 71050},
        {"label": "OCT", "y": 71500},
        {"label": "NOV", "y": 72110},
        {"label": "DEC", "y": 71820}
    ]
    user_data_2023 = [
        {"label": "JAN", "y": 63450},
        {"label": "FEB", "y": 63450},
        {"label": "MAR", "y": 62664},
        {"label": "APR", "y": 68650},
        {"label": "MAY", "y": 53570},
        {"label": "JUN", "y": 75750},
        {"label": "JUL", "y": 69000},
        {"label": "AUG", "y": 65630},
        {"label": "SEP", "y": 71050},
        {"label": "OCT", "y": 45700},
        {"label": "NOV", "y": 75710},
        {"label": "DEC", "y": 73530}
    ]
    return render(request, 'buildings/building.html', {
        'building': building,
        'bills': bills,
        'total_sum': total,
        "user_data_2021": user_data_2021,
        "user_data_2020": user_data_2020,
        "user_data_2023": user_data_2023
    })
