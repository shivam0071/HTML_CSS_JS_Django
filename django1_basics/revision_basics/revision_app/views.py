from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {'my_data':'Data being injected'}
    return render(request,'app1/index.html',context = data)
