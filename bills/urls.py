from django.urls import path

from bills import views


app_name = "bills"

urlpatterns = [
    path("add_bill/<slug:building_slug>/", views.add_bill, name="add_bill"),
    path(
        "add_file_bill/<slug:building_slug>/",
        views.add_file_bill,
        name="add_file_bill",
    ),
    path(
        "load_tariff_and_measure_unit/",
        views.load_tariff_measure_unit,
        name="load_measure_unit",
    ),
    path("add-input/", views.add_input, name="add-input"),
    path("bill_inputs_sum/", views.bill_inputs_sum, name="bill_inputs_sum"),
]
