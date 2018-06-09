from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
# Create your views here.
#Some imports for reducing our efforts
from django.contrib.auth import authenticate,login,logout #one lines for autheticate login and logout
from django.http import HttpResponseRedirect, HttpResponse  #to redirect pages and basic http response
# from django.core.urlresolvers import reverse  #to redirect pages #depricated
from django.urls import reverse
from django.contrib.auth.decorators import login_required #add the decorator to perform certain actions only after
# user is logged in


def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  #to hash the password
            user.save()

            profile = profile_form.save(commit=False) #to avoid collisions that may override existing user
            profile.user = user  # this sets the one to one relation

            if 'profile_pic' in request.FILES: #just a double check
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print('Form Invalid',user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/register.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})


@login_required
def special(request):
    return HttpResponse('You are logged in , Awesome')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  #here username is in the form of login.HTML
        password = request.POST.get('pass')

        user = authenticate(username=username,password=password)  #one line authentication powered by django
        if user:
            if user.is_active:   #a user can be inactive,dead etc
                login(request,user)  #one liner login
                return HttpResponseRedirect(reverse('index'))  #redirect and reverse back to the homepage
            else :
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print ("Some tried to login and failed")
            print (username,password)
            return HttpResponse("invalid login detail ")
    else:
        return render(request,'basic_app/login.html',{})
