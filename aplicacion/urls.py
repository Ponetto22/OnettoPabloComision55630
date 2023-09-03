from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),

    path('buscar_producto/', buscarProducto, name='buscarProducto'),
    path('buscar2/', buscar2, name="buscar2" ),

    path('vendedor/', VendedorList.as_view(), name="vendedor" ),
    path('create_vendedor/', VendedorCreate.as_view(), name="create_vendedor" ),    
    path('update_vendedor/<int:pk>/', VendedorUpdate.as_view(), name="update_vendedor" ),
    path('delete_vendedor/<int:pk>/', VendedorDelete.as_view(), name="delete_vendedor" ),


    path('proveedor/', ProveedorList.as_view(), name="proveedor" ),
    path('create_proveedor/', ProveedorCreate.as_view(), name="create_proveedor" ),    
    path('update_proveedor/<int:pk>/', ProveedorUpdate.as_view(), name="update_proveedor" ),
    path('delete_proveedor/<int:pk>/', ProveedorDelete.as_view(), name="delete_proveedor" ),
    
    path('cliente/', ClienteList.as_view(), name="cliente" ),
    path('create_cliente/', ClienteCreate.as_view(), name="create_cliente" ),    
    path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_cliente" ),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente" ),

    path('producto/', ProductoList.as_view(), name="producto" ),
    path('create_producto/', ProductoCreate.as_view(), name="create_producto" ),    
    path('update_producto/<int:pk>/', ProductoUpdate.as_view(), name="update_producto" ),
    path('delete_producto/<int:pk>/', ProductoDelete.as_view(), name="delete_producto" ),


    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),

   
    path('buscar_vencimiento/', views.buscar_por_vencimiento, name='buscarVencimiento'),
    path('about_me/', about_me, name='about_me'),
    ]