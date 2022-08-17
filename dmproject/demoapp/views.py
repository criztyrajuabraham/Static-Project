from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Teams
# Create your views here.
def home(request):
    obj=Place.objects.all()
    ojb = Teams.objects.all()
    return render(request, "index.html",{'result':obj,'results':ojb})




