from django.shortcuts import render
from TestModel import models 

def hello(request):
    return render(request, 'index.html')

def dbdy(request):
    movelist=models.Test.objects.all()
    return render(request,'movie250.html',{"movelist":movelist})

def jdsj(request):
    movelist=models.JD.objects.all()
    return render(request,'shouji.html',{"movelist":movelist})
