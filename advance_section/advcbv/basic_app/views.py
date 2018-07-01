from django.shortcuts import render
from django.views.generic import View #import for class based views
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return render(request,'index.html',{})

class CBV(View):
    def get(self,request):
        return HttpResponse("Class Based Views")
