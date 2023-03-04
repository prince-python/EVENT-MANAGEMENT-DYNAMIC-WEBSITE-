from django.db import models
import datetime

class Event(models.Model):
    EVENT_BY_COMPANY_NAME=models.CharField(max_length=200)
    CITY_NAME=models.CharField(max_length=200)
    HOTEL_NAME=models.CharField(max_length=200)
    TOTAL_GIRLS_WITH_WORK_AND_DRESS_CODE=models.CharField(max_length=200 ,default=0)
    TOTAL_BOYS_WITH_WORK_AND_DRESS_CODE=models.CharField(max_length=200,default=0)
    DATE_FROM =models.DateField( auto_now_add=False)
    DATE_TO =models.DateField( auto_now_add=False)
    FOOD_INCLUDE=models.BooleanField(default=False)
    PAYMENT_PER_PERSON = models.CharField(max_length=200)
    PAYMENT_MODE=models.CharField(max_length=200,choices=(
        ('ONLINE','ONLINE'),('CASH','CASH'),('CHEQUE','CHEQUE')))
    PAYMENT_STATUS =models.CharField(max_length=200,choices=(
        ('PENDING','PENDING'),('PAID','PAID'),('HALFPAID','HALFPAID')
    ))
    def __str__(self) ->str:
        return self.EVENT_BY_COMPANY_NAME
    
    
class EVENTphotos(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.CASCADE)
    PHOTOS=models.FileField(upload_to='PHOTOS/')
    date_time=models.DateTimeField(  auto_now_add=True)
    def __str__(self) ->str:
        return self.Event.EVENT_BY_COMPANY_NAME
    
class Eventvideos(models.Model):
    Event=models.ForeignKey(Event,on_delete=models.CASCADE)
    VIDEOS=models.FileField(upload_to='VIDEOS/')
    date_time=models.DateTimeField(  auto_now_add=True)
    def __str__(self) ->str:
        return self.Event.EVENT_BY_COMPANY_NAME
    
    
    
    
