from . import models


def agregar_propietario(datos):  
    
    try:
        
        nuevo_propietario=models.Propietario(documento=datos['documento'],\
            nombre=datos['nombre'],\
                    telefono=datos['telefono'],\
                        direccion=datos['direccion'])
        nuevo_propietario.save() 
        return True
    except Exception as e: 

        print(e)
        return False

def consultar_propietario(datos): 
    try:
        propietario=Propietario.objects.get(documento=datos['documento'])
        propietario=json.dumps(propietario.toDict(),ensure_ascii=False)
        return propietario

    except:
        return {}

def modificar_propietario(datos): 
    try:  
        propietario=Propietario.objects.get(documento=datos['documento']) 
        #modificamos atributos
        propietario.documento=datos['documento'] 
        propietario.nombre=datos['nombre']
        propietario.telefono=datos['telefono']
        propietario.direccion=datos['direccion']
        #actualizamos  
        propietario.save()

        return 200

    except:  
        return 401    

def eliminar_propietario(datos): 
    try: 
        propietario=Propietario.objects.get(documento=datos['documento'])
        propietario.delete()

        return 200  
    except:  
        return 404
