from django.db import models

# Create your models here.

class tblUser(models.Model):
    UName = models.CharField(max_length=600)
    UMobile = models.CharField(max_length=600)
    UEmail = models.CharField(max_length=600)
    UState = models.CharField(max_length=600)
    UWallet = models.CharField(max_length=600)
    URefbyCode = models.CharField(max_length=600)

class tblLiveTime(models.Model):
    timed = models.TimeField(max_length=150)

class tblresult1(models.Model):
    resultt1 = models.CharField(max_length=600, default=None, blank=True, null=True)

class tblAGameone(models.Model):
    GameId = models.CharField(max_length=600)
    UMobile = models.CharField(max_length=600)
    Bid1 = models.CharField(max_length=600)
    Bid2 = models.CharField(max_length=600)
    BidResult =  models.CharField(max_length=600)