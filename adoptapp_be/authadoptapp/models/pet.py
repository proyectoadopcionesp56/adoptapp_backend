from django.db import models


class Pet(models.Model):

    class Sizes(models.TextChoices):
        LARGE = 'LG', ('Large')
        MEDIUM = 'MD', ('Medium')
        SMALL = 'SM', ('Small')

    class Status(models.TextChoices):
        REGISTERED = 'RG', ('Registered')
        REQUESTED = 'RQ', ('Requested')
        ADOPTED = 'AP', ('Adopted')
        RETIRED = 'RT', ('Retired')

    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=30)
    species = models.CharField('species', max_length=30)
    size = models.CharField(
        max_length=2,
        choices=Sizes.choices,
        default=Sizes.MEDIUM,
    )
    age = models.IntegerField('age', max_length=2)
    country = models.CharField('country', max_length=30)
    city = models.CharField('city', max_length=30)
    cohabitation_animals = models.BooleanField('cohabitation_animals')
    cohabitation_kids = models.BooleanField('cohabitation_kids')
    pathologies = models.BooleanField('pathologies')
    diseases_drugs = models.CharField('diseases_drugs', max_length=300)
    sterilized = models.BooleanField('sterilized')
    vaccinated = models.BooleanField('vaccinated')
    vaccines = models.CharField('vaccines', max_length=300)
    deworming = models.BooleanField('deworming')
    dewormer = models.CharField('dewormer', max_length=300)
    history = models.CharField('history', max_length=400)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.REGISTERED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)