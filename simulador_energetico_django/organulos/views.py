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



class Organulo_CreateView(CreateView):
    template_name = "organulo/organulo_create.html"
    model = Organulo
    form_class = Organulo_MF

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
       return reverse_lazy(f"organulo_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Organulo_ListView(ListView):
    template_name = "organulo/organulo_list.html"
    model = Organulo
    queryset = Organulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Organulo_UpdateView(UpdateView):
    template_name = "organulo/organulo_update.html"
    model = Organulo
    form_class = Organulo_MF

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
       return reverse_lazy(f"organulo_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Organulo_DetailView(DetailView):
    template_name = "organulo/organulo_detail.html"
    model = Organulo
    queryset = Organulo.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Organulo_DeleteView(DeleteView):
    template_name = "organulo/organulo_delete.html"
    model = Organulo

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"organulo_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class TipoOrganulo_CreateView(CreateView):
    template_name = "tipoorganulo/tipoorganulo_create.html"
    model = TipoOrganulo
    form_class = TipoOrganulo_MF

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
       return reverse_lazy(f"tipoorganulo_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoOrganulo_ListView(ListView):
    template_name = "tipoorganulo/tipoorganulo_list.html"
    model = TipoOrganulo
    queryset = TipoOrganulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoOrganulo_UpdateView(UpdateView):
    template_name = "tipoorganulo/tipoorganulo_update.html"
    model = TipoOrganulo
    form_class = TipoOrganulo_MF

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
       return reverse_lazy(f"tipoorganulo_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoOrganulo_DetailView(DetailView):
    template_name = "tipoorganulo/tipoorganulo_detail.html"
    model = TipoOrganulo
    queryset = TipoOrganulo.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class TipoOrganulo_DeleteView(DeleteView):
    template_name = "tipoorganulo/tipoorganulo_delete.html"
    model = TipoOrganulo

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"tipoorganulo_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Secuenciador_CreateView(CreateView):
    template_name = "secuenciador/secuenciador_create.html"
    model = Secuenciador
    form_class = Secuenciador_MF

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
       return reverse_lazy(f"secuenciador_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Secuenciador_ListView(ListView):
    template_name = "secuenciador/secuenciador_list.html"
    model = Secuenciador
    queryset = Secuenciador.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Secuenciador_UpdateView(UpdateView):
    template_name = "secuenciador/secuenciador_update.html"
    model = Secuenciador
    form_class = Secuenciador_MF

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
       return reverse_lazy(f"secuenciador_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Secuenciador_DetailView(DetailView):
    template_name = "secuenciador/secuenciador_detail.html"
    model = Secuenciador
    queryset = Secuenciador.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Secuenciador_DeleteView(DeleteView):
    template_name = "secuenciador/secuenciador_delete.html"
    model = Secuenciador

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"secuenciador_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class DispositivoControl_CreateView(CreateView):
    template_name = "dispositivocontrol/dispositivocontrol_create.html"
    model = DispositivoControl
    form_class = DispositivoControl_MF

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
       return reverse_lazy(f"dispositivocontrol_ListView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class DispositivoControl_ListView(ListView):
    template_name = "dispositivocontrol/dispositivocontrol_list.html"
    model = DispositivoControl
    queryset = DispositivoControl.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class DispositivoControl_UpdateView(UpdateView):
    template_name = "dispositivocontrol/dispositivocontrol_update.html"
    model = DispositivoControl
    form_class = DispositivoControl_MF

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
       return reverse_lazy(f"dispositivocontrol_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class DispositivoControl_DetailView(DetailView):
    template_name = "dispositivocontrol/dispositivocontrol_detail.html"
    model = DispositivoControl
    queryset = DispositivoControl.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class DispositivoControl_DeleteView(DeleteView):
    template_name = "dispositivocontrol/dispositivocontrol_delete.html"
    model = DispositivoControl

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
       return reverse_lazy(f"dispositivocontrol_ListView")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


