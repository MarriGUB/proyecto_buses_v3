from django import forms
from .models import Mantenimiento, DocumentoVehiculo, Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['placa', 'marca', 'modelo', 'año_fabricacion', 'capacidad_pasajeros', 
                 'numero_chasis', 'numero_motor', 'estado', 'fecha_adquisicion']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: ABC-1234'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Mercedes Benz'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: O500RS'}),
            'año_fabricacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1990, 'max': 2030}),
            'capacidad_pasajeros': forms.NumberInput(attrs={'class': 'form-control', 'min': 10, 'max': 100}),
            'numero_chasis': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_adquisicion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['fecha_mantenimiento', 'tipo', 'descripcion', 'observaciones', 'costo', 'proveedor', 'taller', 'kilometraje']
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Descripción del trabajo realizado...',
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Observaciones adicionales...',
                'class': 'form-control'
            }),
            'costo': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': 0
            }),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'taller': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
        }
        labels = {
            'fecha_mantenimiento': 'Fecha de Mantenimiento',
            'descripcion': 'Descripción',
            'observaciones': 'Observaciones',
            'costo': 'Costo ($)',
            'kilometraje': 'Kilometraje (km)',
        }


class DocumentoVehiculoForm(forms.ModelForm):
    class Meta:
        model = DocumentoVehiculo
        fields = ['tipo', 'numero_documento', 'fecha_emision', 'fecha_vencimiento', 'archivo', 'observaciones']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_emision': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Observaciones del documento...',
                'class': 'form-control'
            }),
        }
        labels = {
            'tipo': 'Tipo de Documento',
            'numero_documento': 'Número de Documento',
            'fecha_emision': 'Fecha de Emisión',
            'fecha_vencimiento': 'Fecha de Vencimiento',
            'archivo': 'Archivo (PDF, imagen, etc.)',
        }