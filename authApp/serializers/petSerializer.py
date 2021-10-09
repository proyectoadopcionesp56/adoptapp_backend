from authApp.models.pet import Pet
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'species',
            'size',
            'age',
            'country',
            'city',
            'cohabitation_animals',
            'cohabitation_kids',
            'pathologies',
            'diseases_drugs',
            'sterilized',
            'vaccinated',
            'vaccines',
            'deworming',
            'dewormer',
            'history',
            'status'
        ]

    def create(self, validated_data):
        petInstance = Pet.objects.create(**validated_data)
        return petInstance

    def to_representation(self, obj):
        pet = Pet.objects.get(id=obj.id)
        return {
            'id': pet.id,
            'name': pet.name,
            'species': pet.species,
            'size': pet.size,
            'age': pet.age,
            'country': pet.country,
            'city': pet.city,
            'cohabitation_animals': pet.cohabitation_animals,
            'cohabitation_kids': pet.cohabitation_kids,
            'pathologies': pet.pathologies,
            'diseases_drugs': pet.diseases_drugs,
            'sterilized': pet.sterilized,
            'vaccinated': pet.vaccinated,
            'vaccines': pet.vaccines,
            'deworming': pet.deworming,
            'dewormer': pet.dewormer,
            'history': pet.history,
            'status': pet.status,
        }
