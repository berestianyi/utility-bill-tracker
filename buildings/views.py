from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from bills.forms import BillsForm, UploadFileBillForm
from bills.models import Bill, BillType
from buildings.forms import BuildingForm
from buildings.models import Building
from buildings.utils import BuildingDataMixin


def index(request):
    form = BillsForm()
    file_form = UploadFileBillForm()

    if request.user.is_authenticated:
        buildings = Building.objects.filter(user=request.user)
    else:
        buildings = []
    return render(request, 'buildings/index.html', {
        'buildings': buildings,
        'form': form,
        'file_form': file_form
    })


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


class BuildingListView(BuildingDataMixin, ListView):
    model = Bill
    context_object_name = 'bills'

    def get_queryset(self):
        building_slug = self.kwargs['building_slug']
        return Bill.objects.filter(building__slug=building_slug).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        building_slug = self.kwargs['building_slug']
        building = Building.objects.get(slug=building_slug)
        context['select_name'] = 'Utility bill type'
        context['building'] = building
        context['bill_types'] = BillType.objects.all()
        context['total_sum'] = Bill.total_sum(building_slug=building_slug)
        context['form'] = BillsForm()
        return context


class BillTypeListView(BuildingDataMixin, ListView):
    model = Bill
    context_object_name = 'bills'

    def get_queryset(self):
        bill_type = BillType.objects.get(slug=self.kwargs['bill_type_slug'])
        bills = Bill.objects.filter(building__slug=self.kwargs['building_slug'])
        return bills.filter(name=bill_type.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        building_slug = self.kwargs['building_slug']
        building = Building.objects.get(slug=building_slug)
        context['select_name'] = BillType.objects.get(slug=self.kwargs['bill_type_slug']).type_name
        context['building'] = building
        context['bill_types'] = BillType.objects.all()
        context['total_sum'] = Bill.total_sum(building_slug=building_slug)
        context['form'] = BillsForm()
        return context



# def building_page(request, building_key):
#     building = Building.objects.get(pk=building_key)
#     bills = Bill.objects.all().filter(building=building_key)
#     total = Bill.total_sum(building_key=building_key)
#     form = BillsForm()
#     user_data_2020 = [
#         {"label": "JAN", "y": 58200},
#         {"label": "FEB", "y": 59110},
#         {"label": "MAR", "y": 60320},
#         {"label": "APR", "y": 61440},
#         {"label": "MAY", "y": 62580},
#         {"label": "JUN", "y": 63190},
#         {"label": "JUL", "y": 64000},
#         {"label": "AUG", "y": 64290},
#         {"label": "SEP", "y": 65530},
#         {"label": "OCT", "y": 65300},
#         {"label": "NOV", "y": 65340},
#         {"label": "DEC", "y": 64530}
#     ]
#     user_data_2021 = [
#         {"label": "JAN", "y": 65100},
#         {"label": "FEB", "y": 66210},
#         {"label": "MAR", "y": 66540},
#         {"label": "APR", "y": 66680},
#         {"label": "MAY", "y": 67500},
#         {"label": "JUN", "y": 68850},
#         {"label": "JUL", "y": 69000},
#         {"label": "AUG", "y": 70130},
#         {"label": "SEP", "y": 71050},
#         {"label": "OCT", "y": 71500},
#         {"label": "NOV", "y": 72110},
#         {"label": "DEC", "y": 71820}
#     ]
#     user_data_2023 = [
#         {"label": "JAN", "y": 63450},
#         {"label": "FEB", "y": 63450},
#         {"label": "MAR", "y": 62664},
#         {"label": "APR", "y": 68650},
#         {"label": "MAY", "y": 53570},
#         {"label": "JUN", "y": 75750},
#         {"label": "JUL", "y": 69000},
#         {"label": "AUG", "y": 65630},
#         {"label": "SEP", "y": 71050},
#         {"label": "OCT", "y": 45700},
#         {"label": "NOV", "y": 75710},
#         {"label": "DEC", "y": 73530}
#     ]
#     return render(request, 'buildings/building.html', {
#         'building': building,
#         'bills': bills,
#         'total_sum': total,
#         'form': form,
#         "user_data_2021": user_data_2021,
#         "user_data_2020": user_data_2020,
#         "user_data_2023": user_data_2023
#     })
