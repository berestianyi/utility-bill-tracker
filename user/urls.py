from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.registration, name='register'),
    path('profile/', views.profile_change, name='profile'),
    path('logout/', views.logout, name='logout'),
]
