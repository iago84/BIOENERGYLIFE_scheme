from django.contrib.auth import views as auth_views
from django.urls import path

from . import views  # Tu archivo de vistas, donde estará la vista de registro
from .views import login_view, logout_view, index_view

urlpatterns = [
	path('', index_view, name='index'),
	path('cliente/dashboard/', views.cliente_dashboard, name='cliente_dashboard'),
	path('proveedor/dashboard/', views.proveedor_dashboard, name='proveedor_dashboard'),
	path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
	path('login', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('register/', views.register_view, name='register'),  # Vista para registrar usuario
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	# Recuperación de contraseña
	path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
	     name='password_reset_confirm'),
	path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
