from django.db import models

# Create your models here.
from django.db import models

"""
Manipulacion de los datos : 

   los modelos se manejan como si fueran objetos de clases , la manipulacion en sql es muy sencilla y se hace de la siguiente manera  
   
   insertar datos en una tabla 
   
   b=Persona(nombre='Juan',edad=23)  
   b.save() 
   
   modificar los datos  
    primero se debe consultar, despues, se altera el atributo y despues se almacena de nuevo 
    
    b=Persona.objects.get(nombre='Juan') 
    b.edad=22 
    b.save() 
    
   eliminar los datos  
   
    primero se debe consultar y despues se elimina  
    
    b=Persona.objects.get(nombre='Juan') 
    b.delete()  
    
    para consultar elementos , se puede hacer con get o filter  
    
    SomeModel.objects.filter(id=id) // filter es como hacer un select where  
    
    tambien podemos hacerlo con get tal como se hizo anteriormente  
    
    para obtener todos los elementos de una tabla se hace con getall  
    
    Persona.objects.getall()
    
    
    
    
    
    
    
   

"""

class Propietario(models.Model): 
    documento=models.CharField(max_length=14,primary_key=True)
    nombre=models.CharField(max_length=50) 
    telefono=models.CharField(max_length=14) 
    direccion=models.CharField(max_length=50) 

    def toDict(self): 
        return {
            "documento":self.documento,
            "nombre":self.nombre ,
            "telefono":self.telefono,
            "direccion":self.direccion



        }


class Mascota(models.Model): 
    propietario=models.ForeignKey('Propietario',on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    edad=models.CharField(max_length=11) 
    especie=models.CharField(max_length=20)
    raza=models.CharField(max_length=30) 
    def toDict(self): 
        return {
            "id":self.id,
            "propietario":self.propietario.documento,
            "nombre":self.nombre ,
            "edad":self.edad,
            "especie":self.especie,
            "raza":self.raza
        }


class Usuario(models.Model):  
    documento=models.CharField(max_length=14,primary_key=True)
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=14)
    direccion=models.CharField(max_length=50)
    email=models.CharField(max_length=50) 
    rol=models.CharField(max_length=20)
    password=models.CharField(max_length=10) 


    def toDict(self): 
        return {
            "documento":self.documento,
            "nombre":self.nombre ,
            "edad":self.edad,
            "telefono":self.telefono,
            "direccion":self.direccion, 
            "email":self.email, 
            "rol":self.rol,
            "password":self.password




        }

class Producto(models.Model): 
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50) 
    tipo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=200) 
    precio=models.IntegerField()
    def toDict(self): 
        return {
            "id":self.id,
            "nombre":self.nombre ,
            "tipo":self.tipo,
            "descripcion":self.descripcion,
            "precio":self.precio



        }


class RegistroClinico(models.Model): 
    mascota=models.ForeignKey('Mascota',on_delete=models.CASCADE) 
    usuario=models.ForeignKey('Usuario',on_delete=models.CASCADE)
    producto=models.ForeignKey('Producto',on_delete=models.CASCADE)
    fecha=models.CharField(max_length=10) 
    detalle=models.CharField(max_length=1000)  

    def toDict(self): 
        return {
            "id":self.id,
            "mascota":self.mascota.id, 
            "usuario":self.usuario.documento, 
            "producto":self.producto.id,
            "fecha":self.fecha,
            "detalle":self.detalle
        }


class Factura(models.Model): 
    propietario=models.ForeignKey('Propietario', on_delete=models.CASCADE) 
    usuario=models.ForeignKey('Usuario',on_delete=models.CASCADE) 
    fecha=models.CharField(max_length=9)
    total=models.IntegerField() 

    def toDict(self) : 
        return { 
            "id":self.id,  
            "propietario":self.propietario.documento, 
            "usuario":self.usuario.documento, 
            "fecha":self.fecha, 
            "total":self.total


        }


class DetalleFactura(models.Model): 
    factura=models.ForeignKey('Factura',on_delete=models.CASCADE) 
    producto=models.ForeignKey('Producto',models.CASCADE) 
    cantidad=models.IntegerField()
    subtotal=models.IntegerField() 

    def toDict(self):
        return{ 
            "factura":self.factura.id, 
            "producto":self.producto.id,
            "cantidad":self.cantidad,  
            "subtotal":self.subtotal

        }
