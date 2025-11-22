from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from .models import Bus, DocumentoVehiculo, Mantenimiento
from .forms import BusForm, MantenimientoForm, DocumentoVehiculoForm

# Vistas de Buses (Proyecto Principal)
class BusListView(ListView):
    model = Bus
    template_name = 'flota/bus_list.html'
    context_object_name = 'buses'
    paginate_by = 20

    def get_queryset(self):
        return Bus.objects.all().order_by('-creado_en')


class BusDetailView(DetailView):
    model = Bus
    template_name = 'flota/bus_detail.html'
    context_object_name = 'bus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bus = self.object
        # Agregar mantenimientos y documentos al contexto
        context['mantenimientos'] = bus.mantenimientos.all().order_by('-fecha_mantenimiento')
        context['documentos'] = bus.documentos.all().order_by('-fecha_vencimiento')
        context['today'] = timezone.now().date()
        return context


class BusCreateView(CreateView):
    model = Bus
    form_class = BusForm
    template_name = 'flota/bus_form.html'
    success_url = reverse_lazy('flota:bus_list')

    def form_valid(self, form):
        messages.success(self.request, f'Bus {form.instance.placa} creado exitosamente.')
        return super().form_valid(form)


class BusUpdateView(UpdateView):
    model = Bus
    form_class = BusForm
    template_name = 'flota/bus_form.html'
    success_url = reverse_lazy('flota:bus_list')

    def form_valid(self, form):
        messages.success(self.request, f'Bus {form.instance.placa} actualizado exitosamente.')
        return super().form_valid(form)


class BusDeleteView(DeleteView):
    model = Bus
    template_name = 'flota/bus_confirm_delete.html'
    success_url = reverse_lazy('flota:bus_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, f'Bus {self.object.placa} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# Vistas de Mantenimientos (De Patentes)
class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'flota/mantenimiento_form.html'
    
    def form_valid(self, form):
        bus = get_object_or_404(Bus, pk=self.kwargs['bus_id'])
        form.instance.bus = bus
        messages.success(self.request, 'Mantenimiento registrado correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('flota:bus_detail', kwargs={'pk': self.kwargs['bus_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus'] = get_object_or_404(Bus, pk=self.kwargs['bus_id'])
        return context


class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'flota/mantenimiento_form.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Mantenimiento actualizado correctamente.')
        return reverse_lazy('flota:bus_detail', kwargs={'pk': self.object.bus.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus'] = self.object.bus
        context['editing'] = True
        return context


class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'flota/mantenimiento_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Mantenimiento eliminado correctamente.')
        return reverse_lazy('flota:bus_detail', kwargs={'pk': self.object.bus.pk})


# Vistas de Documentos (De Patentes)
class DocumentoVehiculoCreateView(CreateView):
    model = DocumentoVehiculo
    form_class = DocumentoVehiculoForm
    template_name = 'flota/documento_form.html'
    
    def form_valid(self, form):
        bus = get_object_or_404(Bus, pk=self.kwargs['bus_id'])
        form.instance.bus = bus
        messages.success(self.request, 'Documento registrado correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('flota:bus_detail', kwargs={'pk': self.kwargs['bus_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus'] = get_object_or_404(Bus, pk=self.kwargs['bus_id'])
        return context


class DocumentoVehiculoUpdateView(UpdateView):
    model = DocumentoVehiculo
    form_class = DocumentoVehiculoForm
    template_name = 'flota/documento_form.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Documento actualizado correctamente.')
        return reverse_lazy('flota:bus_detail', kwargs={'pk': self.object.bus.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus'] = self.object.bus
        context['editing'] = True
        return context


class DocumentoVehiculoDeleteView(DeleteView):
    model = DocumentoVehiculo
    template_name = 'flota/documento_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Documento eliminado correctamente.')
        return reverse_lazy('flota:bus_detail', kwargs={'pk': self.object.bus.pk})