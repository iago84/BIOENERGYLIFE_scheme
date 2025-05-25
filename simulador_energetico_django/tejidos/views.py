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



class Tejido_CreateView(CreateView):
    template_name = "tejido/tejido_create.html"
    model = Tejido
    form_class = Tejido_MF

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
       return reverse_lazy(f"tejido_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Tejido_ListView(ListView):
    template_name = "tejido/tejido_list.html"
    model = Tejido
    queryset = Tejido.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Tejido_UpdateView(UpdateView):
    template_name = "tejido/tejido_update.html"
    model = Tejido
    form_class = Tejido_MF

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
       return reverse_lazy(f"tejido_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Tejido_DetailView(DetailView):
    template_name = "tejido/tejido_detail.html"
    model = Tejido
    queryset = Tejido.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Tejido_DeleteView(DeleteView):
    template_name = "tejido/tejido_delete.html"
    model = Tejido

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"tejido_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class TipoTejido_CreateView(CreateView):
    template_name = "tipotejido/tipotejido_create.html"
    model = TipoTejido
    form_class = TipoTejido_MF

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
       return reverse_lazy(f"tipotejido_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoTejido_ListView(ListView):
    template_name = "tipotejido/tipotejido_list.html"
    model = TipoTejido
    queryset = TipoTejido.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoTejido_UpdateView(UpdateView):
    template_name = "tipotejido/tipotejido_update.html"
    model = TipoTejido
    form_class = TipoTejido_MF

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
       return reverse_lazy(f"tipotejido_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoTejido_DetailView(DetailView):
    template_name = "tipotejido/tipotejido_detail.html"
    model = TipoTejido
    queryset = TipoTejido.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoTejido_DeleteView(DeleteView):
    template_name = "tipotejido/tipotejido_delete.html"
    model = TipoTejido

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"tipotejido_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


