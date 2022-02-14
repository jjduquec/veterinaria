from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json 
# Create your views here.


@csrf_exempt 
def crear(request):
    try:  
        if request.method=='POST': 
            res=HttpResponse() 
            res.status_code=200 
            return res




    except: 
        res=HttpResponse() 
        res.status_code=400
        return res