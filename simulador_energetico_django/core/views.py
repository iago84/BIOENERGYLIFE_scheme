from django.views.generic import *
from django.urls import path,reverse
from .models import *
from .forms import *
from django.core.exceptions import PermissionDenied
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *

class IndexView(TemplateView):
    template_name = "index.html"



class Configuracion_CreateView(CreateView):
    template_name = "configuracion/configuracion_create.html"
    model = Configuracion
    form_class = Configuracion_MF

    def form_valid(self, form):
        # Personaliza lo que sucede cuando el formulario es válido
        self.object = form.save()
        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Personaliza lo que sucede cuando el formulario no es válido
        # Por ejemplo, puedes registrar un mensaje de error
        return super().form_invalid(form)

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"configuracion_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Configuracion_ListView(ListView):
    template_name = "configuracion/configuracion_list.html"
    model = Configuracion
    queryset = Configuracion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Configuracion_UpdateView(UpdateView):
    template_name = "configuracion/configuracion_update.html"
    model = Configuracion
    form_class = Configuracion_MF

    def form_valid(self, form):
        # Personaliza lo que sucede cuando el formulario es válido
        self.object = form.save()
        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Personaliza lo que sucede cuando el formulario no es válido
        # Por ejemplo, puedes registrar un mensaje de error
        return super().form_invalid(form)

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"configuracion_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Configuracion_DetailView(DetailView):
    template_name = "configuracion/configuracion_detail.html"
    model = Configuracion
    queryset = Configuracion.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Configuracion_DeleteView(DeleteView):
    template_name = "configuracion/configuracion_delete.html"
    model = Configuracion

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"configuracion_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Parametro_CreateView(CreateView):
    template_name = "parametro/parametro_create.html"
    model = Parametro
    form_class = Parametro_MF

    def form_valid(self, form):
        # Personaliza lo que sucede cuando el formulario es válido
        self.object = form.save()
        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Personaliza lo que sucede cuando el formulario no es válido
        # Por ejemplo, puedes registrar un mensaje de error
        return super().form_invalid(form)

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"parametro_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Parametro_ListView(ListView):
    template_name = "parametro/parametro_list.html"
    model = Parametro
    queryset = Parametro.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Parametro_UpdateView(UpdateView):
    template_name = "parametro/parametro_update.html"
    model = Parametro
    form_class = Parametro_MF

    def form_valid(self, form):
        # Personaliza lo que sucede cuando el formulario es válido
        self.object = form.save()
        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Personaliza lo que sucede cuando el formulario no es válido
        # Por ejemplo, puedes registrar un mensaje de error
        return super().form_invalid(form)

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"parametro_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Parametro_DetailView(DetailView):
    template_name = "parametro/parametro_detail.html"
    model = Parametro
    queryset = Parametro.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Parametro_DeleteView(DeleteView):
    template_name = "parametro/parametro_delete.html"
    model = Parametro

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"parametro_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Log_CreateView(CreateView):
    template_name = "log/log_create.html"
    model = Log
    form_class = Log_MF

    def form_valid(self, form):
        # Personaliza lo que sucede cuando el formulario es válido
        self.object = form.save()
        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Personaliza lo que sucede cuando el formulario no es válido
        # Por ejemplo, puedes registrar un mensaje de error
        return super().form_invalid(form)

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"log_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Log_ListView(ListView):
    template_name = "log/log_list.html"
    model = Log
    queryset = Log.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Log_UpdateView(UpdateView):
    template_name = "log/log_update.html"
    model = Log
    form_class = Log_MF

    def form_valid(self, form):
        # Personaliza lo que sucede cuando el formulario es válido
        self.object = form.save()
        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Personaliza lo que sucede cuando el formulario no es válido
        # Por ejemplo, puedes registrar un mensaje de error
        return super().form_invalid(form)

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"log_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Log_DetailView(DetailView):
    template_name = "log/log_detail.html"
    model = Log
    queryset = Log.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Log_DeleteView(DeleteView):
    template_name = "log/log_delete.html"
    model = Log

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"log_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


