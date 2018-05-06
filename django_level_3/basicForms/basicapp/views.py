from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':  #if it is a POST call
        form = forms.FormName(request.POST)
        if form.is_valid(): #and if the form is a valid form
        # DO Something
            print('Validation Success!!!')
            print("Name:",form.cleaned_data['name'])
            print("Email:",form.cleaned_data['email'])
            print("Text:",form.cleaned_data['text'])

    return render(request, 'basicapp/forms.html', {'form': form })
