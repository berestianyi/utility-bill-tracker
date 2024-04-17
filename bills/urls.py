from django.urls import path
from bills import views

app_name = 'bills'

urlpatterns = [
    path('load_bill_category/', views.load_bill_category, name='load_bill_category'),
    path('load_measure_unit/', views.load_measure_unit, name='load_measure_unit'),
    path('add-input/', views.add_input, name='add-input'),
    path('bill_inputs_sum/', views.bill_inputs_sum, name='bill_inputs_sum'),
]
