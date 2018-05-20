from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'
#DJANGO seraches for a variable called app_name
urlpatterns = [
    path('other',views.other,name='other'),   #this name is getting used in Templates html
    path('relative_url',views.relative),
]
