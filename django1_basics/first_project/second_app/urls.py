from django.conf.urls import url
from second_app import views2
from django.urls import path
urlpatterns = [
path('second/',views2.index, name = 'index'),
]
