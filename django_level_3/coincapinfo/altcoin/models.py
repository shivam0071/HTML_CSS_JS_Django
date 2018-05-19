from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    name = models.CharField(max_length=30,unique=True)
    symbol = models.CharField(max_length=30,unique=True)
    supply = models.BigIntegerField()
    market_cap = models.BigIntegerField()

    def __str__(self):
        return self.name

class deepInfo(models.Model):
    dname = models.ForeignKey(BasicInfo,on_delete=models.CASCADE)
    dsummary = models.CharField(max_length = 10000)
    dtotal_supply = models.BigIntegerField()
    dwebsite = models.CharField(max_length = 100)

    def __str__(self):
        return self.dwebsite
