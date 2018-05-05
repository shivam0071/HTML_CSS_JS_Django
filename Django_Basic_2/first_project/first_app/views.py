from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage
# Create your views here.
def index(request):
    webpg = AccessRecord.objects.order_by('date')
    data_dict  = {'access_records':webpg}
    return render(request,'first_app/index.html',context=data_dict )
