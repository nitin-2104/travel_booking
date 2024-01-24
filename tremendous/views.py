from django.http import HttpResponse
from django.shortcuts import render 


def homePage(request):
    return HttpResponse(request,"index.html")


def aboutUS(request):
    return HttpResponse("hlw Nitin")