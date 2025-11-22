from django.test import TestCase
from django.utils import timezone
from .models import Viaje
from core.models import Conductor, Lugar
from flota.models import Bus


class ViajeTestCase(TestCase):
    def setUp(self):
        self.conductor = Conductor.objects.create(
            nombre='Juan',
            apellido='Pérez',
            cedula='1234567890',
            email='juan@example.com',
            telefono='0987654321',
            fecha_contratacion='2024-01-01'
        )
        self.bus = Bus.objects.create(
            placa='ABC123',
            modelo='Mercedes Benz',
            año_fabricacion=2020,
            capacidad_pasajeros=50,
            numero_chasis='CH123',
            numero_motor='MO123',
            fecha_adquisicion='2020-05-15'
        )
        self.lugar_origen = Lugar.objects.create(nombre='Quito', ciudad='Quito')
        self.lugar_destino = Lugar.objects.create(nombre='Cuenca', ciudad='Cuenca')

    def test_viaje_creation(self):
        viaje = Viaje.objects.create(
            bus=self.bus,
            conductor=self.conductor,
            lugar_origen=self.lugar_origen,
            lugar_destino=self.lugar_destino,
            fecha_salida=timezone.now(),
            fecha_llegada_estimada=timezone.now()
        )
        self.assertEqual(viaje.estado, 'programado')
