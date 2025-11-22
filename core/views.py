from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms import ModelForm
from django import forms
from django.utils import timezone
from .models import Conductor, Lugar, Pasajero


class ConductorForm(ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre', 'apellido', 'cedula', 'email', 'telefono', 'fecha_contratacion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del conductor'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido del conductor'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de cédula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'fecha_contratacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class LugarForm(ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'ciudad', 'provincia', 'pais', 'latitud', 'longitud']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del lugar',
                'id': 'id_nombre'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ciudad',
                'id': 'id_ciudad'
            }),
            'provincia': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Provincia (opcional)',
                'id': 'id_provincia'
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'País',
                'id': 'id_pais'
            }),
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.000001', 
                'placeholder': 'Latitud (opcional)',
                'id': 'id_latitud'
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.000001', 
                'placeholder': 'Longitud (opcional)',
                'id': 'id_longitud'
            }),
        }


class PasajeroForm(ModelForm):
    class Meta:
        model = Pasajero
        fields = ['nombre_completo', 'rut', 'telefono', 'correo']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del pasajero'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT (ej: 12345678-9)'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
        }


# Vistas para Conductores
class ConductorListView(ListView):
    model = Conductor
    template_name = 'core/conductor_list.html'
    context_object_name = 'conductores'
    paginate_by = 20

    def get_queryset(self):
        return Conductor.objects.all().order_by('-creado_en')


class ConductorDetailView(DetailView):
    model = Conductor
    template_name = 'core/conductor_detail.html'
    context_object_name = 'conductor'


class ConductorCreateView(CreateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'core/conductor_form.html'
    success_url = reverse_lazy('conductor_list')

    def form_valid(self, form):
        messages.success(self.request, f'Conductor {form.instance.nombre} {form.instance.apellido} creado exitosamente.')
        return super().form_valid(form)


class ConductorUpdateView(UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'core/conductor_form.html'
    success_url = reverse_lazy('conductor_list')

    def form_valid(self, form):
        messages.success(self.request, f'Conductor {form.instance.nombre} {form.instance.apellido} actualizado exitosamente.')
        return super().form_valid(form)


class ConductorDeleteView(DeleteView):
    model = Conductor
    template_name = 'core/conductor_confirm_delete.html'
    success_url = reverse_lazy('conductor_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, f'Conductor {self.object.nombre} {self.object.apellido} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# Vistas para Lugares
class LugarListView(ListView):
    model = Lugar
    template_name = 'core/lugar_list.html'
    context_object_name = 'lugares'
    paginate_by = 20

    def get_queryset(self):
        return Lugar.objects.all().order_by('ciudad', 'nombre')


class LugarDetailView(DetailView):
    model = Lugar
    template_name = 'core/lugar_detail.html'
    context_object_name = 'lugar'


class LugarCreateView(CreateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'core/lugar_form.html'
    success_url = reverse_lazy('lugar_list')

    def form_valid(self, form):
        messages.success(self.request, f'Lugar {form.instance.nombre} creado exitosamente.')
        return super().form_valid(form)


class LugarUpdateView(UpdateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'core/lugar_form.html'
    success_url = reverse_lazy('lugar_list')

    def form_valid(self, form):
        messages.success(self.request, f'Lugar {form.instance.nombre} actualizado exitosamente.')
        return super().form_valid(form)


class LugarDeleteView(DeleteView):
    model = Lugar
    template_name = 'core/lugar_confirm_delete.html'
    success_url = reverse_lazy('lugar_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, f'Lugar {self.object.nombre} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# Vistas para Pasajeros
class PasajeroListView(ListView):
    model = Pasajero
    template_name = 'core/pasajero_list.html'
    context_object_name = 'pasajeros'
    paginate_by = 20

    def get_queryset(self):
        return Pasajero.objects.all().order_by('-creado_en')


class PasajeroDetailView(DetailView):
    model = Pasajero
    template_name = 'core/pasajero_detail.html'
    context_object_name = 'pasajero'


class PasajeroCreateView(CreateView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = 'core/pasajero_form.html'
    success_url = reverse_lazy('pasajero_list')

    def form_valid(self, form):
        messages.success(self.request, f'Pasajero {form.instance.nombre_completo} creado exitosamente.')
        return super().form_valid(form)


class PasajeroUpdateView(UpdateView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = 'core/pasajero_form.html'
    success_url = reverse_lazy('pasajero_list')

    def form_valid(self, form):
        messages.success(self.request, f'Pasajero {form.instance.nombre_completo} actualizado exitosamente.')
        return super().form_valid(form)


class PasajeroDeleteView(DeleteView):
    model = Pasajero
    template_name = 'core/pasajero_confirm_delete.html'
    success_url = reverse_lazy('pasajero_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, f'Pasajero {self.object.nombre_completo} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# Vista Home - redirige a buses por defecto
def home_view(request):
    from django.shortcuts import redirect
    return redirect('flota:bus_list')
