from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView #import for class based views
from django.http import HttpResponse
from basic_app.models import School,Student
# Create your views here.

# def index(request):
#     return render(request,'index.html',{})

# class CBV(View):
#     def get(self,request):
#         return HttpResponse("Class Based Views")

#INJECTION
# class IndexView(TemplateView):
#     template_name = 'index.html'
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context


class SchoolListView(ListView):
    model = School

class SchoolDetailView(DetailView):
    model = School
    template_name = 'basic_app/school_details.html'
