
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
import json
from . import controler

# Create your views here.

@csrf_exempt
def crear(request): 
    if request.method=='POST': 
        body=request.body.decode('utf-8')  
        body=json.loads(body) 
        
        if controler.agregar_propietario(body): 
            body={"error":False,"mensaje":"El usuario ha sido creado con exito"}
            body=json.dumps(body)
            
        else:
            body={"error":True,"mensaje":"No es posible crear el usuario, verifique la información "}
            body=json.dumps(body)
            
        response=HttpResponse(body)            
        response.status_code=200 
        return response

    else: 
        response=HttpResponse() 
        response.status_code=400
        return response
