from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Second Page')

def help(request):
    my_dict = {'insert_me':'I am from second app views2.py'}
    return render(request,'second_app/help.html',context=my_dict)
