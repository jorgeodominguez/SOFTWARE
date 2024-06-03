from django.urls import path
from detalle_compras import views

urlpatterns = [
    path('',views.BienvenidaView.as_view(),name='bienvenida'),
    
    #detalle compras
    path('detalle_compras',views.Lista_detalle_compras.as_view(),name='list_detalle_compras'),
    path('detalle_compras/nuevo',views.nuevo_detalle_compras.as_view(),name='nuevo_detalle_compras'),
    path('detalle_compras/editar/<int:pk>',views.editar_detalle_compras.as_view(),name='editar_detalle_compras'),
    path('detalle_compras/eliminar/<int:pk>',views.eliminar_detalle_compras.as_view(),name='eliminar_detalle_compras'),
    
    #compras
    path('compra',views.Lista_compras.as_view(),name='list_compras'),
    path('compra/nuevo',views.nuevo_compras.as_view(),name='nuevo_compras'),
    path('compra/editar/<int:pk>',views.editar_compras.as_view(),name='editar_compras'),
    path('compra/eliminar/<int:pk>',views.eliminar_compras.as_view(),name='eliminar_compras'),
    
    #proveedores
    path('proveedor',views.Lista_proveedores.as_view(),name='list_proveedores'),
    path('proveedor/nuevo',views.nuevo_proveedores.as_view(),name='nuevo_proveedores'),
    path('proveedor/editar/<int:pk>',views.editar_proveedores.as_view(),name='editar_proveedores'),
    path('proveedor/eliminar/<int:pk>',views.eliminar_proveedores.as_view(),name='eliminar_proveedores'),
    
    #articulos
    path('articulo',views.Lista_articulos.as_view(),name='list_articulos'),
    path('articulo/nuevo',views.nuevo_articulos.as_view(),name='nuevo_articulos'),
    path('articulo/editar/<int:pk>',views.editar_articulos.as_view(),name='editar_articulos'),
    path('articulo/eliminar/<int:pk>',views.eliminar_articulos.as_view(),name='eliminar_articulos'),
    
    #marcas
    path('marca',views.Lista_marcas.as_view(),name='list_marcas'),
    path('marca/nuevo',views.nuevo_marcas.as_view(),name='nuevo_marcas'),
    path('marca/editar/<int:pk>',views.editar_marcas.as_view(),name='editar_marcas'),
    path('marca/eliminar/<int:pk>',views.eliminar_marcas.as_view(),name='eliminar_marcas'),

]
