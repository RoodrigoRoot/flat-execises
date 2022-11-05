from django.db import models

# Create your models here.

class Property(models.Model):

    class PropertyType(models.TextChoices):
        APARTMENT = 'DEPARTAMENTO'
        HOUSE = 'CASA'
        CONDO = 'CASA_EN_CONDOMINIO'
        OFFICE = 'OFICINA'
        UNKNOWN = 'DESCONOCIDO'

    asking_price = models.FloatField()
    m2 = models.FloatField()
    property_type = models.CharField(
        choices=PropertyType.choices, max_length=30, blank=True, null=True
    )
    city = models.CharField(
        max_length=100, default='Ciudad de México', blank=True, null=True
    )
    state = models.CharField(
        max_length=100, default='Ciudad de México', blank=True, null=True
    )
    street_name = models.CharField(max_length=100, blank=True, null=True)
    ext_number = models.CharField(max_length=20, blank=True, null=True)
    int_number = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    owner_id = models.CharField(max_length=100, blank=True, null=True)