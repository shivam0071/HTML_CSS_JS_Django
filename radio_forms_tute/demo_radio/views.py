from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    if(request.GET.get('mybtn')):
        print ("Success")
        print (request.GET.get('mybtn'))

    if request.is_ajax():
        #do something
        request_data = request.POST
        return HttpResponse("OK")
    print(forms.CHOICES)
    forms.CHOICES = choices()
    print(forms.CHOICES)
    farm = forms.Radioform()
    if request.method == 'POST':
        farm = forms.Radioform(request.POST)
        if farm.is_valid():
            print('Validation Success!!!')
            print("URL:",farm.cleaned_data['name'])
            print("URL:",farm.cleaned_data['choice_field'])
    # return render(request,'index.html',{'farm':farm})
    return render(request,'index.html',{'farm':['Shaan','is','cool']})
    # return render(request, 'index.html', {'foo': 'bar',})

def choices():
    return (('1', 'First',), ('2', 'Second',),('3', 'Third',), ('4', 'Fourth',))
