from django.db import models
from viajes.models import Viaje


class CostosViaje(models.Model):
    """
    Modelo para registrar y calcular costos de cada viaje.
    """
    viaje = models.OneToOneField(Viaje, on_delete=models.CASCADE, related_name='costos')
    combustible = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    mantenimiento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    peajes = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    otros_costos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    ganancia_neta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    observaciones = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Costo Viaje'
        verbose_name_plural = 'Costos Viajes'

    def save(self, *args, **kwargs):
        # Convertir None a 0 antes de sumar
        combustible = self.combustible or 0
        mantenimiento = self.mantenimiento or 0
        peajes = self.peajes or 0
        otros_costos = self.otros_costos or 0
        
        self.costo_total = combustible + mantenimiento + peajes + otros_costos
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Costos - {self.viaje.bus.placa} ({self.viaje.fecha_salida.date()})"


class Peaje(models.Model):
    """
    Modelo para registrar peajes pagados en viajes.
    """
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name='peajes')
    lugar = models.CharField(max_length=150)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField()
    comprobante = models.CharField(max_length=50, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_pago']
        verbose_name = 'Peaje'
        verbose_name_plural = 'Peajes'

    def __str__(self):
        return f"Peaje en {self.lugar} - ${self.monto}"