from django.contrib import admin
from .models import CostosViaje, Peaje


@admin.register(CostosViaje)
class CostosViajeAdmin(admin.ModelAdmin):
    list_display = ('viaje', 'combustible', 'peajes', 'costo_total', 'ganancia_neta')
    list_filter = ('creado_en',)
    search_fields = ('viaje__bus__placa',)
    fieldsets = (
        ('Viaje', {
            'fields': ('viaje',)
        }),
        ('Desglose de Costos', {
            'fields': ('combustible', 'mantenimiento', 'peajes', 'otros_costos')
        }),
        ('Totales', {
            'fields': ('costo_total', 'ganancia_neta')
        }),
        ('Observaciones', {
            'fields': ('observaciones',)
        }),
    )
    readonly_fields = ('costo_total', 'creado_en', 'actualizado_en')


@admin.register(Peaje)
class PeajeAdmin(admin.ModelAdmin):
    list_display = ('viaje', 'lugar', 'monto', 'fecha_pago', 'comprobante')
    list_filter = ('fecha_pago',)
    search_fields = ('viaje__bus__placa', 'lugar')
    fieldsets = (
        ('Información del Peaje', {
            'fields': ('viaje', 'lugar', 'monto')
        }),
        ('Registro', {
            'fields': ('fecha_pago', 'comprobante')
        }),
    )
