from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import Person

# Create your views here.
def website(request):
    obj= place.objects.all()
    obj1= Person.objects.all()
    return render(request,'index.html',{'result':obj,'output':obj1})
