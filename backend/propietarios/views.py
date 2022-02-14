from django.shortcuts import render
from django.http import HttpResponse 
import json
# Create your views here.


def crear(request): 
    res=HttpResponse()
    res.status_code=200
    return res