# populate_data.py

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lloguerautos.settings')

import django
django.setup()

from django.core.management.base import BaseCommand
from lloguer.models import Automobil, Reserva
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Llena la base de datos con datos ficticios.'

    def handle(self, *args, **kwargs):
        for _ in range(200):
            marca = fake.company()
            modelo = fake.random_element(elements=("SUV", "Sedán", "Camioneta"))
            # Generar matrícula aleatoria con guion
            matricula = self.generate_random_license_plate()
            automovil = Automobil.objects.create(marca=marca, model=modelo, matricula=matricula)

            fecha_inicio = fake.date_between(start_date='-30d', end_date='+30d')
            fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='+30d')
            reserva = Reserva.objects.create(automovil=automovil, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)

        self.stdout.write(self.style.SUCCESS('Datos ficticios generados correctamente.'))

    def generate_random_license_plate(self):
        # Generar matrícula aleatoria con guion
        return str(fake.random_number(digits=4)) + "-" + "".join([fake.random_letter().upper() for _ in range(3)])  # Concatenar números y letras aleatorias en formato de matrícula
