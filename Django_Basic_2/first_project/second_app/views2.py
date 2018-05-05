from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Name
# Create your views here.

def index(request):
    return HttpResponse('Second Page')

def help(request):
    name = Name.objects.all()
    name_dict = {'first_n':name}
    # last_dic = {'last_n':last}
    # email = {'email_n':email}
    # import pdb
    # pdb.set_trace()
    return render(request,'second_app/help.html',context=name_dict)
