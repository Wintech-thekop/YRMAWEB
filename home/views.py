from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'home/home.html')
#    return HttpResponse('<h1>Hello Wintech Thekop</h1>')
# Create your views here.
