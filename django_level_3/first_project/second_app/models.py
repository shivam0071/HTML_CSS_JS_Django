from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=20, unique=True)
    last = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    def __str__(self):
        return self.name
#
# class Last(models.Model):
#     first_name = models.ForeignKey(Name,on_delete=models.CASCADE)
#     last = models.CharField(max_length=20, unique=True)
#     def __str__(self):
#         return self.last
#
# class Email(models.Model):
#     fl_name = models.ForeignKey(Name,on_delete=models.CASCADE)
#     email = models.CharField(max_length=50, unique=True)
#     def __str__(self):
#         return self.email
