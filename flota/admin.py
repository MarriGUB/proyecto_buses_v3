from django.contrib import admin
from .models import Bus, DocumentoVehiculo, Mantenimiento


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'año_fabricacion', 'capacidad_pasajeros', 'estado')
    list_filter = ('estado', 'año_fabricacion')
    search_fields = ('placa', 'modelo', 'numero_chasis')
    fieldsets = (
        ('Información General', {
            'fields': ('placa', 'modelo', 'año_fabricacion', 'capacidad_pasajeros')
        }),
        ('Identificación', {
            'fields': ('numero_chasis', 'numero_motor')
        }),
        ('Estado', {
            'fields': ('estado', 'fecha_adquisicion')
        }),
        ('Metadatos', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('creado_en', 'actualizado_en')


@admin.register(DocumentoVehiculo)
class DocumentoVehiculoAdmin(admin.ModelAdmin):
    list_display = ('bus', 'tipo', 'numero_documento', 'fecha_vencimiento')
    list_filter = ('tipo', 'fecha_vencimiento')
    search_fields = ('bus__placa', 'numero_documento')
    fieldsets = (
        ('Información del Documento', {
            'fields': ('bus', 'tipo', 'numero_documento')
        }),
        ('Fechas', {
            'fields': ('fecha_emision', 'fecha_vencimiento')
        }),
        ('Archivo', {
            'fields': ('archivo',)
        }),
    )


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('bus', 'tipo', 'fecha_mantenimiento', 'costo', 'kilometraje')
    list_filter = ('tipo', 'fecha_mantenimiento')
    search_fields = ('bus__placa', 'descripcion')
    fieldsets = (
        ('Información General', {
            'fields': ('bus', 'tipo', 'descripcion')
        }),
        ('Detalles del Mantenimiento', {
            'fields': ('fecha_mantenimiento', 'kilometraje', 'costo', 'taller')
        }),
        ('Observaciones', {
            'fields': ('observaciones',)
        }),
    )
