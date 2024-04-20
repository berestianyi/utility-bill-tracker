from django.urls import path
from . import views

app_name = 'charts'

urlpatterns = [
    path('chart/', views.chart, name='chart'),
    path('charts/', views.chart, name='33')
]
