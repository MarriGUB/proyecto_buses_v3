from django.test import TestCase
from .models import Bus, DocumentoVehiculo, Mantenimiento


class BusTestCase(TestCase):
    def setUp(self):
        self.bus = Bus.objects.create(
            placa='ABC123',
            modelo='Mercedes Benz O-500',
            año_fabricacion=2020,
            capacidad_pasajeros=50,
            numero_chasis='CH123456789',
            numero_motor='MO123456789',
            fecha_adquisicion='2020-05-15'
        )

    def test_bus_creation(self):
        self.assertEqual(self.bus.placa, 'ABC123')
        self.assertEqual(self.bus.estado, 'activo')
