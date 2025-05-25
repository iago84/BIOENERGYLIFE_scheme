from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from user_management.forms import UserRegisterForm


def index_view(request):
	return render(request, 'index.html')


def login_view(request):
	# Si el usuario ya está autenticado, redirigir a /menu
	if request.user.is_authenticated:
		return redirect('/menu')

	# Si el usuario no está autenticado, mostrar el formulario de login
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)  # Inicia la sesión del usuario
			return redirect('/menu')  # Redirigir a /menu tras login exitoso
	else:
		form = AuthenticationForm()

	return render(request, 'login.html', {'form': form})


def logout_view(request):
	logout(request)
	return redirect('login')


def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)  # Loguea al usuario automáticamente tras registrarse
			messages.success(request, f"Welcome {user.username}, your account was created.")
			return redirect('index')  # Redirige al index
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})


@login_required
def cliente_dashboard(request):
	return render(request, 'cliente_dashboard.html')


@login_required
def proveedor_dashboard(request):
	return render(request, 'proveedor_dashboard.html')


@login_required
def admin_dashboard(request):
	return render(request, 'admin_dashboard.html')


def get_logged_in_user():
    return None