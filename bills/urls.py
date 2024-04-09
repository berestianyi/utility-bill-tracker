from django.urls import path
from bills import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:building_key>/', views.add_bill, name='add_bill'),
    path('load_bill_category/', views.load_bill_category, name='load_bill_category'),
    path('load_measure_unit/', views.load_measure_unit, name='load_measure_unit'),
    path('add_building/', views.add_building, name='add_building'),
    path('building/<int:building_key>/', views.building_page, name='building'),
    path('add-input/', views.add_input, name='add-input'),
]
