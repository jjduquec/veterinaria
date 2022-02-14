from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .controlers import *
import json
# Create your views here. 

#inicio usuario
@csrf_exempt
def login(request): 
    try:
    #verificamos el metodo con el que se hizo la peticion 
        if request.method=='POST': 
            #decodificamos el contenido del cuerpo
            body=request.body.decode('utf-8')  
            #convertimos de json a diccionario
            body=json.loads(body) 
            #enviamos a controlador 
            res=HttpResponse()
            res.status_code=inicio_sesion(body)
            return  res
    except:  
        res=HttpResponse() 
        res.status_code=400 
        return res 


@csrf_exempt 
def usuario(request): 
   
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar usuario  
            data=consultar_usuario(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un usuario 
            response.status_code=agregar_usuario(body) 
            return response 

        elif request.method=='PUT': 
            print('entro a actualizar')
            response=HttpResponse() 
            #vamos a modificar un usuario  
            response.status_code=modificar_usuario(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar usuario  
            response=HttpResponse() 
            response.status_code=eliminar_usuario(body) 
            return response  
        
        


    
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response         
#fin usuario  

#inicio propietario
@csrf_exempt 
def propietario(request): 
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar usuario  
            data=consultar_propietario(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un usuario 
            response.status_code=agregar_propietario(body) 
            return response 

        elif request.method=='PUT': 
            print('entro a actualizar')
            response=HttpResponse() 
            #vamos a modificar un usuario  
            response.status_code=modificar_propietario(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar usuario  
            response=HttpResponse() 
            response.status_code=eliminar_propietario(body) 
            return response  
            
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response         
#fin propietario  

#inicio producto  
@csrf_exempt  
def producto(request): 
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar usuario  
            data=consultar_producto(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un usuario 
            response.status_code=agregar_producto(body) 
            return response 

        elif request.method=='PUT': 
            print('entro a actualizar')
            response=HttpResponse() 
            #vamos a modificar un usuario  
            response.status_code=modificar_producto(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar usuario  
            response=HttpResponse() 
            response.status_code=eliminar_producto(body) 
            return response  
            
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response    
# fin producto

#inicio mascota
@csrf_exempt  
def mascota(request):  
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar usuario  
            data=consultar_mascota(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un usuario 
            response.status_code=agregar_mascota(body) 
            return response 

        elif request.method=='PUT': 
            response=HttpResponse() 
            #vamos a modificar un usuario  
            response.status_code=modificar_mascota(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar usuario  
            response=HttpResponse() 
            response.status_code=eliminar_mascota(body) 
            return response  
            
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response   

@csrf_exempt  
def mascotas(request): 
    try:  
        body=request.body.decode('utf-8') 
        body=json.loads(body) 
        if request.method=='GET':
            #indentacion
            data=consultar_mascotas(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        else:  
            raise Exception('400 Bad request')


    except Exception as excepcion: 
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response 
        
# fin mascota 


#inicio registro clinico  
@csrf_exempt  
def registro(request):  
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar usuario  
            data=consultar_registro(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un usuario 
            response.status_code=agregar_registro(body) 
            return response 

        elif request.method=='PUT': 
            response=HttpResponse() 
            #vamos a modificar un usuario  
            response.status_code=modificar_registro(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar usuario  
            response=HttpResponse() 
            response.status_code=eliminar_registro(body) 
            return response  
            
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response 

def registros(request): 
    try:  
        body=request.body.decode('utf-8') 
        body=json.loads(body) 
        if request.method=='GET':
            #indentacion
            data=consultar_registros(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        else:  
            raise Exception('400 Bad request')


    except Exception as excepcion: 
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response 

# fin registro Clinico  

#inicio factura 
@csrf_exempt 
def factura(request):  
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar usuario  
            data=consultar_factura(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un usuario 
            response.status_code=agregar_factura(body)  
            return response 

        elif request.method=='PUT': 
            response=HttpResponse() 
            #vamos a modificar un usuario  
            response.status_code=modificar_factura(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar usuario  
            response=HttpResponse() 
            response.status_code=eliminar_factura(body) 
            return response  
            
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response 


@csrf_exempt 
def detalle(request):  
    try:
        #decodificamos la informacion y la transformamos  
        body=request.body.decode('utf-8') 
        body=json.loads(body)
        #determinamos la operacion 
        
        if request.method=='GET': 
            #vamos a consultar detalle 
            data=consultar_detalle(body)
            if data=={}: 
                response=HttpResponse()  
                response.status_code=404
            else:  
                response=HttpResponse(data)
            
            return response 
        elif request.method=='POST': 
            response=HttpResponse()  
            #vamos a crear un detalle
            response.status_code=agregar_detalle(body)  
            return response 

        elif request.method=='PUT': 
            response=HttpResponse() 
            #vamos a modificar detalle
            response.status_code=modificar_detalle(body) 
            return response

        elif request.method=='DELETE': 
            #vamos a eliminar detalle
            response=HttpResponse() 
            response.status_code=eliminar_detalle(body) 
            return response  
            
    except Exception as excepcion:  
        print(excepcion)
        response=HttpResponse() 
        response.status_code=400
        return response 

