from django.db import models
from core.models import Conductor, Lugar, Pasajero
from flota.models import Bus


class Viaje(models.Model):
    """
    Modelo para registrar viajes planificados de la flota.
    """
    ESTADO_VIAJE = [
        ('programado', 'Programado'),
        ('en_curso', 'En Curso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT, related_name='viajes')
    conductor = models.ForeignKey(Conductor, on_delete=models.PROTECT, related_name='viajes')
    lugar_origen = models.ForeignKey(Lugar, on_delete=models.PROTECT, related_name='viajes_origen')
    lugar_destino = models.ForeignKey(Lugar, on_delete=models.PROTECT, related_name='viajes_destino')
    fecha_salida = models.DateTimeField()
    fecha_llegada_estimada = models.DateTimeField()
    fecha_llegada_real = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_VIAJE, default='programado')
    latitud_origen = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_origen = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitud_destino = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_destino = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pasajeros = models.ManyToManyField(Pasajero, through='ViajePasajero', blank=True, related_name='viajes')
    pasajeros_confirmados = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_salida']
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

    def __str__(self):
        return f"{self.bus.placa} - {self.lugar_origen.nombre} -> {self.lugar_destino.nombre} ({self.fecha_salida.date()})"
    
    def get_pasajeros_count(self):
        return self.pasajeros.count()


class ViajePasajero(models.Model):
    """
    Modelo intermedio para la relación entre Viaje y Pasajero.
    """
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    asiento = models.CharField(max_length=10, blank=True, null=True)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('viaje', 'pasajero')
        verbose_name = 'Pasajero en Viaje'
        verbose_name_plural = 'Pasajeros en Viajes'
    
    def __str__(self):
        return f"{self.pasajero.nombre_completo} - {self.viaje}"
