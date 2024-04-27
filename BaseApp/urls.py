from django.urls import path, include
from .views import *

urlpatterns = [
    path('CreateNewAcc', CreateNewAcc, name='CreateNewAcc'),
    path('', login_view, name='login_view'),
    path('home', home, name='home'),
    path('Logout', logout_view, name='Logout'),
    path('search/', search_view, name='search'),
    path('detail_view/', detail_view, name='detail_view'),
    path('add_feedback/', add_feedback, name='add_feedback'),
    path('error_page/', error_page, name='error_page'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
]