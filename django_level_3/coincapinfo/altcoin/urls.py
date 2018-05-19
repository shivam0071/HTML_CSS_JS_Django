from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('allcoins/',views.allcoins),
    path('submitNewCoin/',views.submit_new),
    path('singlecoin/',views.singlecoin),
    ]
