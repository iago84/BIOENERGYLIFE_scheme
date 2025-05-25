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



class Celula_CreateView(CreateView):
    template_name = "celula/celula_create.html"
    model = Celula
    form_class = Celula_MF

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
       return reverse_lazy(f"celula_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Celula_ListView(ListView):
    template_name = "celula/celula_list.html"
    model = Celula
    queryset = Celula.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Celula_UpdateView(UpdateView):
    template_name = "celula/celula_update.html"
    model = Celula
    form_class = Celula_MF

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
       return reverse_lazy(f"celula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Celula_DetailView(DetailView):
    template_name = "celula/celula_detail.html"
    model = Celula
    queryset = Celula.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Celula_DeleteView(DeleteView):
    template_name = "celula/celula_delete.html"
    model = Celula

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"celula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class EstadoCelula_CreateView(CreateView):
    template_name = "estadocelula/estadocelula_create.html"
    model = EstadoCelula
    form_class = EstadoCelula_MF

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
       return reverse_lazy(f"estadocelula_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EstadoCelula_ListView(ListView):
    template_name = "estadocelula/estadocelula_list.html"
    model = EstadoCelula
    queryset = EstadoCelula.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EstadoCelula_UpdateView(UpdateView):
    template_name = "estadocelula/estadocelula_update.html"
    model = EstadoCelula
    form_class = EstadoCelula_MF

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
       return reverse_lazy(f"estadocelula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EstadoCelula_DetailView(DetailView):
    template_name = "estadocelula/estadocelula_detail.html"
    model = EstadoCelula
    queryset = EstadoCelula.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EstadoCelula_DeleteView(DeleteView):
    template_name = "estadocelula/estadocelula_delete.html"
    model = EstadoCelula

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"estadocelula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class EvolucionCelula_CreateView(CreateView):
    template_name = "evolucioncelula/evolucioncelula_create.html"
    model = EvolucionCelula
    form_class = EvolucionCelula_MF

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
       return reverse_lazy(f"evolucioncelula_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EvolucionCelula_ListView(ListView):
    template_name = "evolucioncelula/evolucioncelula_list.html"
    model = EvolucionCelula
    queryset = EvolucionCelula.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EvolucionCelula_UpdateView(UpdateView):
    template_name = "evolucioncelula/evolucioncelula_update.html"
    model = EvolucionCelula
    form_class = EvolucionCelula_MF

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
       return reverse_lazy(f"evolucioncelula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EvolucionCelula_DetailView(DetailView):
    template_name = "evolucioncelula/evolucioncelula_detail.html"
    model = EvolucionCelula
    queryset = EvolucionCelula.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class EvolucionCelula_DeleteView(DeleteView):
    template_name = "evolucioncelula/evolucioncelula_delete.html"
    model = EvolucionCelula

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"evolucioncelula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class UbicacionCelula_CreateView(CreateView):
    template_name = "ubicacioncelula/ubicacioncelula_create.html"
    model = UbicacionCelula
    form_class = UbicacionCelula_MF

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
       return reverse_lazy(f"ubicacioncelula_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UbicacionCelula_ListView(ListView):
    template_name = "ubicacioncelula/ubicacioncelula_list.html"
    model = UbicacionCelula
    queryset = UbicacionCelula.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UbicacionCelula_UpdateView(UpdateView):
    template_name = "ubicacioncelula/ubicacioncelula_update.html"
    model = UbicacionCelula
    form_class = UbicacionCelula_MF

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
       return reverse_lazy(f"ubicacioncelula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UbicacionCelula_DetailView(DetailView):
    template_name = "ubicacioncelula/ubicacioncelula_detail.html"
    model = UbicacionCelula
    queryset = UbicacionCelula.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UbicacionCelula_DeleteView(DeleteView):
    template_name = "ubicacioncelula/ubicacioncelula_delete.html"
    model = UbicacionCelula

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"ubicacioncelula_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


