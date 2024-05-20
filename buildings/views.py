from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView

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
    return render(
        request,
        "buildings/index.html",
        {"buildings": buildings, "form": form, "file_form": file_form},
    )


def add_building(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            new_building = form.save(commit=False)
            new_building.user = request.user
            new_building.save()
            form.save_m2m()
            return redirect("buildings:index")
    else:
        form = BuildingForm()
    return render(request, "buildings/add_building.html", {"form": form})


class BuildingListView(BuildingDataMixin, ListView):
    model = Bill
    context_object_name = "bills"

    def get_queryset(self):
        building_slug = self.kwargs["building_slug"]
        return Bill.objects.filter(building__slug=building_slug).order_by(
            "-created_at"
        )

    def get_context_data(self, **kwargs):
        context = self.get_common_context(**kwargs)
        context["select_name"] = "Utility bill type"
        return context


class BillTypeListView(BuildingDataMixin, ListView):
    model = Bill
    context_object_name = "bills"

    def get_queryset(self):
        bill_type = BillType.objects.get(slug=self.kwargs["bill_type_slug"])
        bills = Bill.objects.filter(
            building__slug=self.kwargs["building_slug"]
        )
        return bills.filter(name=bill_type.id)

    def get_context_data(self, **kwargs):
        context = self.get_common_context(**kwargs)
        context["select_name"] = BillType.objects.get(
            slug=self.kwargs["bill_type_slug"]
        ).type_name
        return context


def change_building(request, building_slug):
    building = get_object_or_404(Building, slug=building_slug)
    if request.method == "POST":
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect("buildings:building", building_slug)
    else:
        form = BuildingForm(instance=building)
    return render(request, "buildings/add_building.html", {'change_form': form})


def htmx_form_change(request, building_slug):
    building = get_object_or_404(Building, slug=building_slug)
    form = BuildingForm(instance=Building.objects.get(slug=building_slug))
    return render(request, 'buildings/htmx/change_building.html', context={
        'change_form': form,
        'building': building})
