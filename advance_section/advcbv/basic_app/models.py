from django.db import models
from django.urls import reverse  #added reverse, note that this is updated in django version 2.0
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 250)
    principal = models.CharField(max_length = 250)
    location = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

    def get_absolute_url (self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length = 250)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students') #used in school details html to get
    #the student data from School models itself...cool

    def __str__(self):
        return self.name
