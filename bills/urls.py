from django.urls import path
from bills import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_bill, name='add_bill'),
    path('building/<int:building_key>/', views.building, name='building')
]
