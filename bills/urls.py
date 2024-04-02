from django.urls import path
from bills import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
]