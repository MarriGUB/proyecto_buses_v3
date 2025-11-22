from django.contrib import admin
from .models import Conductor, Lugar


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'cedula', 'email', 'activo')
    list_filter = ('activo', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido', 'cedula', 'email')
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'cedula', 'email', 'telefono')
        }),
        ('Empleo', {
            'fields': ('fecha_contratacion', 'activo')
        }),
        ('Metadatos', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('creado_en', 'actualizado_en')


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'provincia', 'pais')
    list_filter = ('ciudad', 'pais')
    search_fields = ('nombre', 'ciudad')
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'ciudad', 'provincia', 'pais')
        }),
        ('Ubicación (Coordenadas)', {
            'fields': ('latitud', 'longitud'),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('creado_en',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('creado_en',)
