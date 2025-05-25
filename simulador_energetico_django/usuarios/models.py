from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    nivel_acceso = models.CharField(
        max_length=20,
        choices=[("user", "Usuario"), ("admin", "Administrador"), ("viewer", "Solo lectura")],
        default="user"
    )

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    perfil = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True, blank=True)
    energia_maxima_autorizada = models.FloatField(default=0.0)
    configuracion_personal = models.JSONField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_usuario_set',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_usuario_permissions',
        blank=True,
        help_text='Permisos específicos para este usuario.'
    )

    def __str__(self):
        return self.username
