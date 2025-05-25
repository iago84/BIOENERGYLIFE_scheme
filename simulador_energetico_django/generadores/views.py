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



class Generador_CreateView(CreateView):
    template_name = "generador/generador_create.html"
    model = Generador
    form_class = Generador_MF

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
       return reverse_lazy(f"generador_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Generador_ListView(ListView):
    template_name = "generador/generador_list.html"
    model = Generador
    queryset = Generador.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Generador_UpdateView(UpdateView):
    template_name = "generador/generador_update.html"
    model = Generador
    form_class = Generador_MF

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
       return reverse_lazy(f"generador_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Generador_DetailView(DetailView):
    template_name = "generador/generador_detail.html"
    model = Generador
    queryset = Generador.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Generador_DeleteView(DeleteView):
    template_name = "generador/generador_delete.html"
    model = Generador

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"generador_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class TipoGenerador_CreateView(CreateView):
    template_name = "tipogenerador/tipogenerador_create.html"
    model = TipoGenerador
    form_class = TipoGenerador_MF

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
       return reverse_lazy(f"tipogenerador_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoGenerador_ListView(ListView):
    template_name = "tipogenerador/tipogenerador_list.html"
    model = TipoGenerador
    queryset = TipoGenerador.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoGenerador_UpdateView(UpdateView):
    template_name = "tipogenerador/tipogenerador_update.html"
    model = TipoGenerador
    form_class = TipoGenerador_MF

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
       return reverse_lazy(f"tipogenerador_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoGenerador_DetailView(DetailView):
    template_name = "tipogenerador/tipogenerador_detail.html"
    model = TipoGenerador
    queryset = TipoGenerador.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoGenerador_DeleteView(DeleteView):
    template_name = "tipogenerador/tipogenerador_delete.html"
    model = TipoGenerador

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"tipogenerador_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Arranque_CreateView(CreateView):
    template_name = "arranque/arranque_create.html"
    model = Arranque
    form_class = Arranque_MF

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
       return reverse_lazy(f"arranque_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Arranque_ListView(ListView):
    template_name = "arranque/arranque_list.html"
    model = Arranque
    queryset = Arranque.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Arranque_UpdateView(UpdateView):
    template_name = "arranque/arranque_update.html"
    model = Arranque
    form_class = Arranque_MF

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
       return reverse_lazy(f"arranque_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Arranque_DetailView(DetailView):
    template_name = "arranque/arranque_detail.html"
    model = Arranque
    queryset = Arranque.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Arranque_DeleteView(DeleteView):
    template_name = "arranque/arranque_delete.html"
    model = Arranque

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"arranque_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Rack_CreateView(CreateView):
    template_name = "rack/rack_create.html"
    model = Rack
    form_class = Rack_MF

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
       return reverse_lazy(f"rack_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Rack_ListView(ListView):
    template_name = "rack/rack_list.html"
    model = Rack
    queryset = Rack.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Rack_UpdateView(UpdateView):
    template_name = "rack/rack_update.html"
    model = Rack
    form_class = Rack_MF

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
       return reverse_lazy(f"rack_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Rack_DetailView(DetailView):
    template_name = "rack/rack_detail.html"
    model = Rack
    queryset = Rack.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Rack_DeleteView(DeleteView):
    template_name = "rack/rack_delete.html"
    model = Rack

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"rack_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


