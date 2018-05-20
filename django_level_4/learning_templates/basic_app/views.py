from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'name':'Hello World','num':100}
    return render(request,'basic_app/index.html',data)

def other(request):
    return render(request,'basic_app/other.html',{})

def relative(request):
    return render(request,'basic_app/relative_url.html',{})
