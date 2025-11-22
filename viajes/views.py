from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.http import JsonResponse
from django.db import transaction
from .models import Viaje, ViajePasajero
from core.models import Conductor, Lugar, Pasajero
from flota.models import Bus


class ViajeForm(ModelForm):
    class Meta:
        model = Viaje
        fields = [
            'bus', 'conductor', 'lugar_origen', 'lugar_destino',
            'fecha_salida', 'fecha_llegada_estimada', 'fecha_llegada_real',
            'estado', 'pasajeros_confirmados', 'observaciones'
        ]
        widgets = {
            'bus': forms.Select(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-control'}),
            'lugar_origen': forms.Select(attrs={'class': 'form-control'}),
            'lugar_destino': forms.Select(attrs={'class': 'form-control'}),
            'fecha_salida': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Fecha y hora de salida'
            }),
            'fecha_llegada_estimada': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Fecha y hora estimada de llegada'
            }),
            'fecha_llegada_real': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Fecha y hora real de llegada (opcional)'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'pasajeros_confirmados': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Número de pasajeros confirmados'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales (opcional)'
            }),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Capturar coordenadas del lugar de origen
        if instance.lugar_origen:
            instance.latitud_origen = instance.lugar_origen.latitud
            instance.longitud_origen = instance.lugar_origen.longitud
        # Capturar coordenadas del lugar de destino
        if instance.lugar_destino:
            instance.latitud_destino = instance.lugar_destino.latitud
            instance.longitud_destino = instance.lugar_destino.longitud
        if commit:
            instance.save()
        return instance


# Vistas para Viajes
class ViajeListView(ListView):
    model = Viaje
    template_name = 'viajes/viaje_list.html'
    context_object_name = 'viajes'
    paginate_by = 20

    def get_queryset(self):
        return Viaje.objects.all().order_by('-fecha_salida')


class ViajeDetailView(DetailView):
    model = Viaje
    template_name = 'viajes/viaje_detail.html'
    context_object_name = 'viaje'


class ViajeCreateView(CreateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'viajes/viaje_form.html'
    success_url = reverse_lazy('viajes:viaje_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            f'Viaje {form.instance.bus.placa} creado exitosamente.'
        )
        return super().form_valid(form)


class ViajeUpdateView(UpdateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'viajes/viaje_form.html'
    success_url = reverse_lazy('viajes:viaje_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            f'Viaje {form.instance.bus.placa} actualizado exitosamente.'
        )
        return super().form_valid(form)


class ViajeDeleteView(DeleteView):
    model = Viaje
    template_name = 'viajes/viaje_confirm_delete.html'
    success_url = reverse_lazy('viajes:viaje_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(
            request,
            f'Viaje {self.object.bus.placa} eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)


# Vistas para manejar pasajeros en viajes
def viaje_pasajeros_view(request, pk):
    """
    Vista para mostrar y manejar pasajeros de un viaje específico.
    """
    viaje = get_object_or_404(Viaje, pk=pk)
    pasajeros_en_viaje = ViajePasajero.objects.filter(viaje=viaje).select_related('pasajero')
    pasajeros_disponibles = Pasajero.objects.exclude(id__in=viaje.pasajeros.values_list('id', flat=True))
    
    context = {
        'viaje': viaje,
        'pasajeros_en_viaje': pasajeros_en_viaje,
        'pasajeros_disponibles': pasajeros_disponibles,
    }
    return render(request, 'viajes/viaje_pasajeros.html', context)


def agregar_pasajero_viaje(request, pk):
    """
    Vista para agregar un pasajero a un viaje.
    """
    if request.method == 'POST':
        viaje = get_object_or_404(Viaje, pk=pk)
        pasajero_id = request.POST.get('pasajero_id')
        asiento = request.POST.get('asiento')
        observaciones = request.POST.get('observaciones', '')
        
        try:
            pasajero = get_object_or_404(Pasajero, pk=pasajero_id)
            
            # Verificar si el pasajero ya está en el viaje
            if ViajePasajero.objects.filter(viaje=viaje, pasajero=pasajero).exists():
                messages.error(request, f'El pasajero {pasajero.nombre_completo} ya está registrado en este viaje.')
            else:
                # Verificar capacidad del bus
                if viaje.get_pasajeros_count() >= viaje.bus.capacidad_pasajeros:
                    messages.error(request, 'El bus ha alcanzado su capacidad máxima de pasajeros.')
                else:
                    ViajePasajero.objects.create(
                        viaje=viaje,
                        pasajero=pasajero,
                        asiento=asiento,
                        observaciones=observaciones
                    )
                    
                    # Actualizar el contador de pasajeros confirmados
                    viaje.pasajeros_confirmados = viaje.get_pasajeros_count()
                    viaje.save()
                    
                    messages.success(request, f'Pasajero {pasajero.nombre_completo} agregado al viaje exitosamente.')
                    
        except Pasajero.DoesNotExist:
            messages.error(request, 'Pasajero no encontrado.')
        except Exception as e:
            messages.error(request, f'Error al agregar pasajero: {str(e)}')
    
    return redirect('viajes:viaje_pasajeros', pk=pk)


def quitar_pasajero_viaje(request, pk, pasajero_pk):
    """
    Vista para quitar un pasajero de un viaje.
    """
    if request.method == 'POST':
        viaje = get_object_or_404(Viaje, pk=pk)
        pasajero = get_object_or_404(Pasajero, pk=pasajero_pk)
        
        try:
            viaje_pasajero = ViajePasajero.objects.get(viaje=viaje, pasajero=pasajero)
            viaje_pasajero.delete()
            
            # Actualizar el contador de pasajeros confirmados
            viaje.pasajeros_confirmados = viaje.get_pasajeros_count()
            viaje.save()
            
            messages.success(request, f'Pasajero {pasajero.nombre_completo} removido del viaje exitosamente.')
            
        except ViajePasajero.DoesNotExist:
            messages.error(request, 'El pasajero no está registrado en este viaje.')
        except Exception as e:
            messages.error(request, f'Error al remover pasajero: {str(e)}')
    
    return redirect('viajes:viaje_pasajeros', pk=pk)


def editar_pasajero_viaje(request, pk, pasajero_pk):
    """
    Vista para editar información de un pasajero en un viaje.
    """
    viaje = get_object_or_404(Viaje, pk=pk)
    pasajero = get_object_or_404(Pasajero, pk=pasajero_pk)
    viaje_pasajero = get_object_or_404(ViajePasajero, viaje=viaje, pasajero=pasajero)
    
    if request.method == 'POST':
        asiento = request.POST.get('asiento')
        observaciones = request.POST.get('observaciones', '')
        
        viaje_pasajero.asiento = asiento
        viaje_pasajero.observaciones = observaciones
        viaje_pasajero.save()
        
        messages.success(request, f'Información del pasajero {pasajero.nombre_completo} actualizada exitosamente.')
        return redirect('viajes:viaje_pasajeros', pk=pk)
    
    context = {
        'viaje': viaje,
        'pasajero': pasajero,
        'viaje_pasajero': viaje_pasajero,
    }
    return render(request, 'viajes/editar_pasajero_viaje.html', context)
