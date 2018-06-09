from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  #one to one so that now this model has all the fields such as
    #username, email password first name and last name now lets add some more fields
    portfolio_site = models.URLField(blank=True) #blank True means that its not necessary to fill this field
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username
