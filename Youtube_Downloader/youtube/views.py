from django.shortcuts import render
from . import forms
from pytube import YouTube
# Create your views here.

def index(request):
    # if request.method == 'POST':
    #     print('found a form')
    #     request.
    #     return render(request,'youtube\index.html',{})
    # else:
    #     return render(request,'youtube\index.html',{})
    form = forms.Youform()
    if request.method == 'POST':  #if it is a POST call
        form = forms.Youform(request.POST)
        if form.is_valid(): #and if the form is a valid form
        # DO Something
            print('Validation Success!!!')
            try:
                print("URL:",form.cleaned_data['url'])
                yt = YouTube(form.cleaned_data['url'])
                print (yt.title)
                stream = yt.streams.first() #lets take 1st for example
                stream.download() #You can give a path here
            except:
                print("Faulty URL")
            # yt.streams.all() #Choose a stream


    return render(request, 'youtube/index.html', {'form': form })
