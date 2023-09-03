from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Producto, Cliente, Proveedor, Vendedor
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuariosForm, UserEditForm, AvatarFormulario

from .models import Avatar


# Create your views here.
def home(request):
    return render(request, "aplicacion/base.html")


class VendedorList(LoginRequiredMixin,ListView):
    model = Vendedor

class VendedorCreate(LoginRequiredMixin,CreateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('vendedor')

class VendedorUpdate(LoginRequiredMixin,UpdateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('vendedor')

class VendedorDelete(LoginRequiredMixin,DeleteView):
    model = Vendedor
    success_url = reverse_lazy('vendedor')




class ProveedorList(LoginRequiredMixin,ListView):
    model = Proveedor

class ProveedorCreate(LoginRequiredMixin,CreateView):
    model = Proveedor
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('proveedor')

class ProveedorUpdate(LoginRequiredMixin,UpdateView):
    model = Proveedor
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('proveedor')

class ProveedorDelete(LoginRequiredMixin,DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedor')




class ProductoList(LoginRequiredMixin,ListView):
    model = Producto

class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    fields = ['nombre', 'codigo', 'precio', 'vencimiento']
    success_url = reverse_lazy('producto')

class ProductoUpdate(LoginRequiredMixin,UpdateView):
    model = Producto
    fields = ['nombre', 'codigo', 'precio', 'vencimiento']
    success_url = reverse_lazy('producto')

class ProductoDelete(LoginRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('producto')


class ClienteList(LoginRequiredMixin,ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin,CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('cliente')

class ClienteUpdate(LoginRequiredMixin,UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('cliente')

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente')


@login_required
def producto(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, "aplicacion/producto.html", contexto)
@login_required
def buscarProducto(request):
    return render(request, "aplicacion/buscarProducto.html")
@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        producto = Producto.objects.filter(nombre__icontains=patron)
        contexto = {'productos': producto, 'titulo': f'Productos que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/producto.html", contexto)
    return HttpResponse("No se ingresó nada para buscar")




#__________________ Login / Logout / Registracion____________

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from .models import Producto

@login_required
def buscar_por_vencimiento(request):
    hoy = timezone.now().date()
    seis_meses_desde_hoy = hoy + timedelta(days=180)
    
    productos_por_vencer = Producto.objects.filter(vencimiento__gte=hoy, vencimiento__lte=seis_meses_desde_hoy)
    
    contexto = {
        'productos': productos_por_vencer,
        'titulo': 'Productos por vencer en los próximos 6 meses'
    }
    
    return render(request, "aplicacion/buscarVencimiento.html", contexto)


def about_me(request):    
    informacion_personal = {
        'nombre': ' Pablo Andres Onetto ' ,
        'biografia': 'Hola, voy a presentarme, soy Pablo de Montevideo, Uruguay. Tengo 38 años. Soy técnico en informática en el area de hardware, actualemnte me estoy enfocando en estudiar programación, espero les guste mi web.',
        'foto': '/media/foto2.jpg'

    }
    
    return render(request, 'aplicacion/about_me.html', {'informacion_personal': informacion_personal})

