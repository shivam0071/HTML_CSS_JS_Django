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
class IndexView(TemplateView):
    template_name = 'index.html'
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION'
    #     return context


class SchoolListView(ListView):
    context_object_name = 'schools'  #context
    model = School
    # here the list view automatically returns school_list which we use as context in html files
    # School got lower cased and _list got added hence school_list
    # we can overwrite the name of the context by context_object_name = 'schools'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'  #by default it returns 'school' as context
    model = School
    template_name = 'basic_app/school_details.html'
