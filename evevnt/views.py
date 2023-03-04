from .models import *
from django.shortcuts import render

def index(request):
    data=EVENTphotos.objects.all()
    return render(request,"index.html",{'data':data})
