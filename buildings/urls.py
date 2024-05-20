from django.urls import path

from . import views


app_name = "buildings"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_building/", views.add_building, name="add_building"),
    path(
        "building/<slug:building_slug>/",
        views.BuildingListView.as_view(),
        name="building",
    ),
    path(
        "building/<slug:building_slug>/<slug:bill_type_slug>/",
        views.BillTypeListView.as_view(),
        name="bill_type",
    ),
    path(
        "building/<slug:building_slug>/change",
        views.change_building,
        name="change_building",
    ),
    path(
        "building/<slug:building_slug>/htmx_form_change",
        views.htmx_form_change,
        name="htmx_form_change",
    )
]
