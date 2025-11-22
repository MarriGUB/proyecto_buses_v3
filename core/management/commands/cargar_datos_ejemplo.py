from django.core.management.base import BaseCommand
from core.models import Conductor
from datetime import date

class Command(BaseCommand):
    help = 'Carga datos de ejemplo para conductores'

    def handle(self, *args, **options):
        # Crear conductores de ejemplo como en el mockup
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
                    self.style.SUCCESS(f'Conductor {conductor.nombre} {conductor.apellido} creado exitosamente')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Conductor {conductor.nombre} {conductor.apellido} ya existe')
                )

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados exitosamente'))