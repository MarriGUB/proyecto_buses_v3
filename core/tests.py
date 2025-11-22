from django.test import TestCase
from .models import Conductor, Lugar


class ConductorTestCase(TestCase):
    def setUp(self):
        self.conductor = Conductor.objects.create(
            nombre='Juan',
            apellido='Pérez',
            cedula='1234567890',
            email='juan@example.com',
            telefono='0987654321',
            fecha_contratacion='2024-01-01'
        )

    def test_conductor_creation(self):
        self.assertEqual(self.conductor.nombre, 'Juan')
        self.assertTrue(self.conductor.activo)


class LugarTestCase(TestCase):
    def setUp(self):
        self.lugar = Lugar.objects.create(
            nombre='Terminal Central',
            ciudad='Quito'
        )

    def test_lugar_creation(self):
        self.assertEqual(self.lugar.nombre, 'Terminal Central')
