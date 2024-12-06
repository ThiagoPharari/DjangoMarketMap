from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, Usuario, Producto
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admin = Admin.objects.get(username=username, password=password)
                request.session['admin_id'] = admin.id
                return redirect('menu_usuarios')
            except Admin.DoesNotExist:
                messages.error(request, "Credenciales incorrectas")
    return render(request, 'usuarios/login.html', {'form': form})

def menu_usuarios(request):
    if 'admin_id' not in request.session:
        return redirect('login')

    usuarios_activos = Usuario.objects.filter(estado='activo')
    return render(request, 'usuarios/menu_usuarios.html', {'usuarios': usuarios_activos})

def editar_usuario(request, usuario_id):
    if 'admin_id' not in request.session:
        return redirect('login')

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.apellido = request.POST.get('apellido')
        usuario.correo = request.POST.get('correo')
        usuario.dni = request.POST.get('dni')
        usuario.numero = request.POST.get('numero')
        usuario.save()
        return redirect('menu_usuarios')

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, usuario_id):
    if 'admin_id' not in request.session:
        return redirect('login')

    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('menu_usuarios')

def banear_usuario(request, usuario_id):
    if 'admin_id' not in request.session:
        return redirect('login')

    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.estado = 'baneado'
    usuario.save()
    return redirect('menu_usuarios')

def menu_usuarios_baneados(request):
    if 'admin_id' not in request.session:
        return redirect('login')

    usuarios_baneados = Usuario.objects.filter(estado='baneado')
    return render(request, 'usuarios/menu_baneados.html', {'usuarios': usuarios_baneados})

def menu_productos(request):
    if 'admin_id' not in request.session:
        return redirect('login')

    productos = Producto.objects.all()
    return render(request, 'usuarios/menu_productos.html', {'productos': productos})

def editar_producto(request, producto_id):
    if 'admin_id' not in request.session:
        return redirect('login')

    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.save()
        return redirect('menu_productos')

    return render(request, 'usuarios/editar_producto.html', {'producto': producto})

def eliminar_producto(request, producto_id):
    if 'admin_id' not in request.session:
        return redirect('login')

    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('menu_productos')

