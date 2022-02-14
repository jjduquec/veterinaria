from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Propietario) 
class PropietarioAdmin(admin.ModelAdmin):  
    list_display=('documento','nombre','telefono','direccion')
    search_field=('documento','nombre')

@admin.register(models.Mascota) 
class MascotaAdmin(admin.ModelAdmin):  
    list_display=('id','nombre','edad','propietario','raza','especie')
    search_field=('propietario','nombre','raza','especie') 


@admin.register(models.Usuario) 
class UsuarioAdmin(admin.ModelAdmin):  
    list_display=('documento','nombre','edad','rol') 
    search_field=('documento','rol','nombre')


@admin.register(models.Producto) 
class ProductoAdmin(admin.ModelAdmin): 
    list_display=('id','nombre','tipo','precio') 
    search_field=('id','nombre','tipo','precio') 


@admin.register(models.RegistroClinico) 
class RegistroClinicoAdmin(admin.ModelAdmin): 
    list_display=('id','mascota','usuario','producto','fecha','detalle') 
    search_field=('id','mascota','usuario','producto','fecha')


@admin.register(models.Factura) 
class FacturaAdmin(admin.ModelAdmin): 
    list_display=('id','propietario','usuario','fecha','total') 
    search_field=('id','propietario','fecha','usuario','total') 

@admin.register(models.DetalleFactura) 
class DetalleFacturaAdmin(admin.ModelAdmin): 
    list_display=('factura','producto','cantidad','subtotal') 
    search_field=('factura','producto','cantidad','subtotal') 
    