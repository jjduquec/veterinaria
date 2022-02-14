from .models import *
import json


"""
        200: OK 
        401: No autorizado 
        404: No encontrado
        405: No aceptado  permisos usuario/ problemas integridad  datos
""" 
#controladores USUARIO

def inicio_sesion(datos):  

   

    try:

        usuario=Usuario.objects.get(documento=datos['documento'])  
        if usuario.password==datos['password']:
            return 200
        else:
            return 401

    except:  
        return 404
    




def agregar_usuario(datos):  
    try:
        nuevo_usuario=Usuario(documento=datos['documento'],\
            nombre=datos['nombre'],\
                edad=datos['edad'],\
                    telefono=datos['telefono'],\
                        direccion=datos['direccion'],\
                            email=datos['email'],\
                                rol=datos['rol'],\
                                    password=datos['password'])
        nuevo_usuario.save() 
        return 201
    except:  
        return 405


def consultar_usuario(datos): 
    try:
        usuario=Usuario.objects.get(documento=datos['documento'])
        usuario=json.dumps(usuario.toDict(),ensure_ascii=False)
        return usuario

    except:
        return {}

def modificar_usuario(datos): 
    try:  
        usuario=Usuario.objects.get(documento=datos['documento']) 
        #modificamos atributos
        usuario.documento=datos['documento'] 
        usuario.nombre=datos['nombre']
        usuario.edad=datos['edad']
        usuario.telefono=datos['telefono']
        usuario.direccion=datos['direccion']
        usuario.email=datos['email']
        usuario.rol=datos['rol']
        usuario.password=datos['password']
        #actualizamos  
        usuario.save()

        return 200







    except:  
        return 401    

def eliminar_usuario(datos): 
    try: 
        usuario=Usuario.objects.get(documento=datos['documento'])
        usuario.delete()

        return 200  
    except:  
        return 404


# Fin controladores USUARIO   

#Inicio Propietario 
def agregar_propietario(datos):  
    
    try:
        print(datos)
        nuevo_propietario=Propietario(documento=datos['documento'],\
            nombre=datos['nombre'],\
                edad=datos['edad'],\
                    telefono=datos['telefono'],\
                        direccion=datos['direccion'])
        nuevo_propietario.save() 
        return 201
    except:  
        return 405

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


#fin Propietario  

#inicio Producto 

def agregar_producto(datos):  
    
    try:
        nuevo_producto=Producto(
            nombre=datos['nombre'],\
                tipo=datos['tipo'],\
                    descripcion=datos['descripcion'],\
                        precio=datos['precio'])
        nuevo_producto.save() 
        return 201
    except:  
        return 405

def consultar_producto(datos): 
    try:
        producto=Producto.objects.get(nombre=datos['nombre'])
        producto=json.dumps(producto.toDict(),ensure_ascii=False)
        return producto

    except:
        return {}

def modificar_producto(datos): 
    try:  
        producto=Producto.objects.get(id=datos['id']) 
        #modificamos atributos
        producto.nombre=datos['nombre']
        producto.tipo=datos['tipo']
        producto.descripcion=datos['descripcion'] 
        producto.precio=datos['precio']
        #actualizamos  
        producto.save()

        return 200

    except:  
        return 401    

def eliminar_producto(datos): 
    try: 
        producto=Producto.objects.get(nombre=datos['nombre'])
        producto.delete()

        return 200  
    except:  
        return 404




#fin Producto 

# inicio Mascota  
def agregar_mascota(datos): 
    try:
        nueva_mascota=Mascota(
            propietario=Propietario.objects.get(documento=datos['propietario']),\
            nombre=datos['nombre'],\
                edad=datos['edad'],\
                    especie=datos['especie'],\
                        raza=datos['raza'])
        nueva_mascota.save() 
        return 201
    except Exception as e:   
        return 405 
def consultar_mascota(datos): 
    try:
        mascota=Mascota.objects.get(propietario=\
            Propietario.objects.get(documento=datos['propietario'])\
            ,nombre=datos['nombre'])
        mascota=json.dumps(mascota.toDict(),ensure_ascii=False)
        return mascota

    except:
        return {}

def modificar_mascota(datos): 
    try:  
        mascota=Mascota.objects.get(propietario=\
            Propietario.objects.get(documento=datos['propietario'])\
            ,nombre=datos['nombre'])
        #modificamos atributos
        mascota.nombre=datos['nombre']
        mascota.edad=datos['edad']
        mascota.especie=datos['especie']
        mascota.raza=datos['raza']
        #actualizamos  
        mascota.save()
        return 200

    except:  
        return 401  

def eliminar_mascota(datos): 
    try: 
        mascota=Mascota.objects.get(propietario=\
            Propietario.objects.get(documento=datos['propietario'])\
            ,nombre=datos['nombre'])
        mascota.delete()

        return 200  
    except:  
        return 404
def consultar_mascotas(datos): 
    try:
        lista_mascotas=[] 
        mascotas=\
            Mascota.objects.filter(\
            propietario=Propietario.objects.get(documento=datos['propietario']))  
        for mascota in mascotas: 
            lista_mascotas.append(mascota.toDict())     
        return json.dumps({'mascotas':lista_mascotas},ensure_ascii=False)            
    except:  
        return {}

# fin Mascota 

#inicio Registros   
def agregar_registro(datos):
    try:
        nuevo_registro=RegistroClinico(\
            mascota=Mascota.objects.get(id=datos['mascota']),\
                usuario=Usuario.objects.get(documento=datos['usuario']),\
                    producto=Producto.objects.get(id=datos['producto']),\
                        fecha=datos['fecha'],\
                            detalle=datos['detalle']    
        )
        nuevo_registro.save()  
        return 201
    except Exception as e:   
        print(e)
        return 405  
def modificar_registro(datos): 
    try:  
        registro=RegistroClinico.objects.get(id=datos['id'])

        #modificamos atributos
        registro.mascota=Mascota.objects.get(id=datos['mascota'])
        registro.usuario=Usuario.objects.get(documento=datos['usuario']) 
        registro.producto=Producto.objects.get(id=datos['producto'])  
        registro.fecha=datos['fecha'] 
        registro.detalle=datos['detalle'] 
        #actualizamos  
        registro.save()
        return 200

    except Exception as e:   
        print(e)
        return 401 

def consultar_registro(datos): 
    try:
        registro=RegistroClinico.objects.get(id=datos['registro'])
        registro=json.dumps(registro.toDict(),ensure_ascii=False)
        return registro

    except Exception as e: 
        print(e)
        return {}

def eliminar_registro(datos): 
    try: 
        registro=RegistroClinico.objects.get(id=datos['id'])
        registro.delete() 

        return 200  
    except:  
        return 404 

def consultar_registros(datos): 
    try:
        lista_registros=[] 
        registros=\
            RegistroClinico.objects.filter(\
            mascota=Mascota.objects.get(id=datos['id']))  
        for registro in registros: 
            lista_registros.append(registro.toDict())     
        return json.dumps({'registros':lista_registros},ensure_ascii=False)            
    except:  
        return {}


#fin Registros  

#inicio factura 
def agregar_factura(datos):
    try:
        nueva_factura=Factura(\
            propietario=Propietario.objects.get(documento=datos['propietario']),\
                usuario=Usuario.objects.get(documento=datos['usuario']),\
                        fecha=datos['fecha'],\
                            total=datos['total']    
        )
        nueva_factura.save()  

        #almacenamiento de los detalles  
        detalles=datos['detalles'] 
        for detalle in detalles:  
            nuevo_detalle=DetalleFactura(\
            factura=Factura.objects.get(id=nueva_factura.id),\
                producto=Producto.objects.get(id=detalle['producto']),\
                        cantidad=detalle['cantidad'],\
                            subtotal=detalle['subtotal']    
        )
            nuevo_detalle.save()
                

        return 201
    except Exception as e:   
        print(e)
        return 405  
def modificar_factura(datos): 
    try:  
        factura=Factura.objects.get(id=datos['id'])

        #modificamos atributos
        factura.propietario=Propietario.objects.get(documento=datos['propietario'])
        factura.usuario=Usuario.objects.get(documento=datos['usuario']) 
        factura.fecha=datos['fecha'] 
        factura.total=datos['total']  
        #actualizamos  
        factura.save()
        return 200

    except Exception as e:   
        print(e)
        return 401 

def consultar_factura(datos): 
    try:
        factura=Factura.objects.get(id=datos['id'])
        factura=json.dumps(factura.toDict(),ensure_ascii=False)
        return factura

    except Exception as e: 
        print(e)
        return {}

def eliminar_factura(datos): 
    try: 
        factura=Factura.objects.get(id=datos['id'])
        factura.delete() 

        return 200  
    except:  
        return 404 
"""
def consultar_registros(datos): 
    try:
        lista_registros=[] 
        registros=\
            RegistroClinico.objects.filter(\
            mascota=Mascota.objects.get(id=datos['id']))  
        for registro in registros: 
            lista_registros.append(registro.toDict())     
        return json.dumps({'registros':lista_registros},ensure_ascii=False)            
    except:  
        return {}

"""
#fin factura  

#inicio detalles  
def agregar_detalle(datos):
    try:
        nuevo_detallle=DetalleFactura(\
            factura=Factura.objects.get(id=datos['factura']),\
                producto=Producto.objects.get(id=datos['producto']),\
                        cantidad=datos['cantidad'],\
                            subtotal=datos['subtotal']    
        )
        nuevo_detallle.save()
        return 201
    except Exception as e:   
        print(e)
        return 405  
def modificar_detalle(datos): 
    try:  
        detalle=DetalleFactura.objects.get(\
            factura=Factura.objects.get(id=datos['factura']),\
                producto=Producto.objects.get(id=datos['producto'])
                        
            
            )

        #modificamos atributos
        detalle.factura=Factura.objects.get(id=datos['factura'])
        detalle.producto=Producto.objects.get(id=datos['producto']) 
        detalle.cantidad=datos['cantidad'] 
        detalle.subtotal=datos['subtotal']  
        #actualizamos  
        detalle.save()
        return 200

    except Exception as e:   
        print(e)
        return 401 

def consultar_detalle(datos): 
    try:
        detalle=DetalleFactura.objects.get(\
            factura=Factura.objects.get(id=datos['factura']), 
            producto=Producto.objects.get(id=datos['producto'])

        )
        detalle=json.dumps(detalle.toDict(),ensure_ascii=False)
        return detalle

    except Exception as e: 
        print(e)
        return {}

def eliminar_detalle(datos): 
    try: 
        detalle=DetalleFactura.objects.get(\
            factura=Factura.objects.get(id=datos['factura']), 
            producto=Producto.objects.get(id=datos['producto'])

        )

        detalle.delete() 

        return 200  
    except Exception as e:   
        print(e)
        return 404 

#fin detalles 