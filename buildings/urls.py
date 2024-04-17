from django.urls import path
from . import views

app_name = 'buildings'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_building/', views.add_building, name='add_building'),
    path('building/<int:building_key>/', views.building_page, name='building'),
]
