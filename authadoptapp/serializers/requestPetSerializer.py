from authadoptapp.models.requestPet import RequestPet
from authadoptapp.models.pet import Pet
from authadoptapp.models.user import User
from rest_framework import serializers
from authadoptapp.serializers.petSerializer import PetSerializer
from authadoptapp.serializers.userSerializer import UserSerializer


class RequestPetSerializer(serializers.ModelSerializer):
    # pet = PetSerializer()
    # user = UserSerializer()

    class Meta:
        model = RequestPet
        fields = [
            'id',
            'user',
            'pet',
            'created_at',
            'request_kind',
            'finalized_at',
        ]

    def create(self, validated_data):

        pet = validated_data.pop('pet')

        petData = Pet.objects.get(id=pet.id)

        # print("AAAAA ")
        user = validated_data.pop('user')
        # print("BBBBB ")
        userData = User.objects.get(id=user.id)
        # user = userData.

        requestPetInstance = RequestPet.objects.create(
            user=userData, pet=petData, **validated_data)

        return requestPetInstance

    def to_representation(self, obj):
        requestPet = RequestPet.objects.get(id=obj.id)

        image_url = ""
        if(requestPet.pet.image.url):
            image_url = requestPet.pet.image.url

        return {
            'id': requestPet.id,
            'user': requestPet.user.id,
            'pet': {
                'id': requestPet.pet.id,
                'name': requestPet.pet.name,
                # 'species': pet.species,
                # 'size': pet.size,
                # 'age': pet.age,
                # 'country': pet.country,
                # 'city': pet.city,
                # 'cohabitation_animals': pet.cohabitation_animals,
                # 'cohabitation_kids': pet.cohabitation_kids,
                # 'pathologies': pet.pathologies,
                # 'diseases_drugs': pet.diseases_drugs,
                # 'sterilized': pet.sterilized,
                # 'vaccinated': pet.vaccinated,
                # 'vaccines': pet.vaccines,
                # 'deworming': pet.deworming,
                # 'dewormer': pet.dewormer,
                # 'history': pet.history,
                'status': requestPet.pet.status,
                'image': image_url,
                # 'created_at': pet.created_at,
                # 'updated_at': pet.updated_at
            },
            'created_at': requestPet.created_at,
            'request_kind': requestPet.request_kind,
            'finalized_at': requestPet.finalized_at,
        }
