# Crear datos de ejemplo adicionales para otras entidades
from django.core.management.base import BaseCommand
from flota.models import Bus
from core.models import Conductor, Lugar
from datetime import date

class Command(BaseCommand):
    help = 'Carga datos de ejemplo completos para el sistema'

    def handle(self, *args, **options):
        # Crear conductores de ejemplo
        conductores_data = [
            {
                'nombre': 'Juan',
                'apellido': 'Pérez',
                'cedula': '1234567890',
                'email': 'jperez@empresa.com',
                'telefono': '+56987654321',
                'fecha_contratacion': date(2023, 1, 15),
                'activo': True
            },
            {
                'nombre': 'Ana',
                'apellido': 'Gómez',
                'cedula': '0987654321',
                'email': 'agomez@empresa.com',
                'telefono': '+56912345678',
                'fecha_contratacion': date(2023, 3, 10),
                'activo': True
            }
        ]

        for data in conductores_data:
            conductor, created = Conductor.objects.get_or_create(
                cedula=data['cedula'],
                defaults=data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Conductor {conductor.nombre} {conductor.apellido} creado')
                )

        # Crear buses de ejemplo
        buses_data = [
            {
                'placa': 'ABC-123',
                'modelo': 'Mercedes Benz O500RS',
                'año_fabricacion': 2020,
                'capacidad_pasajeros': 45,
                'numero_chasis': 'MB123456789',
                'numero_motor': 'MB987654321',
                'estado': 'activo',
                'fecha_adquisicion': date(2020, 5, 15)
            },
            {
                'placa': 'XYZ-789',
                'modelo': 'Volvo B11R',
                'año_fabricacion': 2021,
                'capacidad_pasajeros': 50,
                'numero_chasis': 'VO123456789',
                'numero_motor': 'VO987654321',
                'estado': 'activo',
                'fecha_adquisicion': date(2021, 8, 20)
            }
        ]

        for data in buses_data:
            bus, created = Bus.objects.get_or_create(
                placa=data['placa'],
                defaults=data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Bus {bus.placa} creado')
                )

        # Crear lugares de ejemplo
        lugares_data = [
            {
                'nombre': 'Terminal Norte',
                'ciudad': 'Quito',
                'provincia': 'Pichincha',
                'pais': 'Ecuador',
                'latitud': -0.1807,
                'longitud': -78.4678
            },
            {
                'nombre': 'Terminal Sur',
                'ciudad': 'Guayaquil',
                'provincia': 'Guayas',
                'pais': 'Ecuador',
                'latitud': -2.1894,
                'longitud': -79.8890
            }
        ]

        for data in lugares_data:
            lugar, created = Lugar.objects.get_or_create(
                nombre=data['nombre'],
                ciudad=data['ciudad'],
                defaults=data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Lugar {lugar.nombre} creado')
                )

        self.stdout.write(self.style.SUCCESS('Todos los datos de ejemplo cargados exitosamente'))