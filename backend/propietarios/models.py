from django.db import models

# Create your models here.
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