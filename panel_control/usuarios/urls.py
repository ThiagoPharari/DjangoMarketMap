from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('usuarios/', views.menu_usuarios, name='menu_usuarios'),
    path('usuario/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuario/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuario/banear/<int:usuario_id>/', views.banear_usuario, name='banear_usuario'),
    path('usuarios/baneados/', views.menu_usuarios_baneados, name='menu_usuarios_baneados'),
    path('productos/', views.menu_productos, name='menu_productos'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
