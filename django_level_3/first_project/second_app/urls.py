from django.conf.urls import url
from second_app import views2
from django.urls import path
urlpatterns = [
path('',views2.help, name = 'help'),
]
