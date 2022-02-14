from django.urls import path 

from . import views 

urlpatterns=[
    path('login',views.login),
    path('usuario',views.usuario),
    path('propietario',views.propietario), 
    path('producto',views.producto),
    path('mascota',views.mascota),
    path('mascotas',views.mascotas), 
    path('registro',views.registro),
    path('registros',views.registros), 
    path('factura',views.factura),
    path('detalle',views.detalle),


    



]

