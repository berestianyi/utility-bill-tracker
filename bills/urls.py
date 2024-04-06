from django.urls import path
from bills import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_bill, name='add_bill'),
    path('add_building/', views.add_building, name='add_building'),
    path('building/<int:building_key>/', views.building_page, name='building'),
    path('add-input/', views.add_input, name='add-input'),
]
