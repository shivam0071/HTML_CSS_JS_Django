from django.shortcuts import render
from django.http import HttpResponse
from .models import BasicInfo,deepInfo
from . import forms
# Create your views here.
# def index(request):
#     return HttpResponse('Index')
def find(coin_name):
    """
    From Index to SingleCoin
    """
    ddata = deepInfo.objects.filter(dname__name=coin_name) #dname is taking its value from name (foreign key)
    data = BasicInfo.objects.filter(name = coin_name).values_list('symbol',flat=True)
    ddeep = {'coin':ddata, 'symbol': data }
    return ddeep

def index(request):
    if request.method == 'POST':  #if it is a POST call
        key = request.POST.get('coin','butt123')
        print (key)
        if key.split()[0].isalpha():
                print('Validation Success!!!')
                print(request.POST.get('coin'))
                coin_name = request.POST.get('coin')
                ddeep = find(coin_name)
                return render(request,'altcoin/singlecoin.html',context = ddeep)
        else:
                data = BasicInfo.objects.all()
                alts = {'altcoins':data}
                return render(request,'altcoin/allcoins.html',context = alts)

    return render(request,'altcoin/index.html',{})


def allcoins(request):
    data = BasicInfo.objects.all()
    alts = {'altcoins':data}
    return render(request,'altcoin/allcoins.html',context = alts)


def singlecoin(request,coin_name):
    '''
    Sending only the required coin
    '''
    ddata = deepInfo.objects.filter(dname__name=coin_name) #dname is taking its value from name (foreign key)
    data = BasicInfo.objects.filter(name = coin_name)
    data = BasicInfo.objects.filter(name = coin_name).values_list('symbol',flat=True)
    ddeep = {'coin':ddata, 'symbol': data }
    return render(request,'altcoin/singlecoin.html',context = ddeep)


def submit_new(request,initial=True):
    # name = Name.objects.all()
    # name_dict = {'first_n':name}
    basic_form = forms.BasicInfoForm()
    deep_form = forms.DeepInfoForm()
    forms_dict = {'forms':basic_form, 'forms2':deep_form}
    print('')
    if request.method == 'POST':
            user_form = forms.BasicInfoForm(request.POST)
            deep_form2 = forms.DeepInfoForm(request.POST)
            print('user_form:-',user_form)
            if user_form.is_valid():
                print('Validation Success!!')
                print(user_form.cleaned_data['name'])
                print(user_form.cleaned_data['symbol'])
                print(user_form.cleaned_data['supply'])
                user_form.save()

            elif deep_form2.is_valid():
                print('Validation Success!!')
                print(deep_form2.cleaned_data['dsummary'])
                print(deep_form2.cleaned_data['dwebsite'])
                print(deep_form2.cleaned_data['dname'])
                deep_form2.save()
            else:
                print('user form is not valid')
                #
                # return submit_new(request)

    return render(request,'altcoin/forms.html',context=forms_dict)
