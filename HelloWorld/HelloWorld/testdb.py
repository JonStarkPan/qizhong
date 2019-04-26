# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
from TestModel.models import JD
# 数据库操作
def testdb(request):
    response = ""
    response1 = ""
    list = Test.objects.all()
    for var in list:
        response1 +=str(var.id) + " "+var.movie_name + " " +"</p>"
    list2 = JD.objects.all()
    for var in list2:
        response1 += var.link + " " + var.price + " " + var.name + " " + var.comment + " "+"</p>"
    response = response1
    return HttpResponse("<p>" + response + "</p>")

