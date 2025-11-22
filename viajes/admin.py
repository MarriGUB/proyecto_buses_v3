from django.contrib import admin
from .models import Viaje


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('bus', 'conductor', 'lugar_origen', 'lugar_destino', 'fecha_salida', 'estado')
    list_filter = ('estado', 'fecha_salida')
    search_fields = ('bus__placa', 'conductor__apellido', 'lugar_origen__nombre', 'lugar_destino__nombre')
    fieldsets = (
        ('Información del Viaje', {
            'fields': ('bus', 'conductor')
        }),
        ('Ruta', {
            'fields': ('lugar_origen', 'lugar_destino')
        }),
        ('Coordenadas Origen', {
            'fields': ('latitud_origen', 'longitud_origen'),
            'classes': ('collapse',)
        }),
        ('Coordenadas Destino', {
            'fields': ('latitud_destino', 'longitud_destino'),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_salida', 'fecha_llegada_estimada', 'fecha_llegada_real')
        }),
        ('Operación', {
            'fields': ('estado', 'pasajeros_confirmados', 'observaciones')
        }),
        ('Timestamps', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('creado_en', 'actualizado_en', 'latitud_origen', 'longitud_origen', 'latitud_destino', 'longitud_destino')
