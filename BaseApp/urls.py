from django.urls import path, include
from .views import *

urlpatterns = [
    path('CreateNewAcc', CreateNewAcc, name='CreateNewAcc'),
    path('', login_view, name='login_view'),
    path('home', home, name='home'),
    path('Logout', logout_view, name='Logout')
]