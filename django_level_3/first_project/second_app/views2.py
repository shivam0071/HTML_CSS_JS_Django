from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Name
from . import forms
# Create your views here.

def index(request):
    return HttpResponse('Second Page')

def help(request):
    # name = Name.objects.all()
    # name_dict = {'first_n':name}
    user_form = forms.UserForm()

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        if user_form.is_valid():
            print('Validation Success!!')
            print(user_form.cleaned_data['name'])
            print(user_form.cleaned_data['last'])
            print(user_form.cleaned_data['email'])
            user_form.save()
            return index(request)
    return render(request,'second_app/help.html',{'form':user_form})
