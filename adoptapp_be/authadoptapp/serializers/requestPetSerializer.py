from authadoptapp.models.requestPet import RequestPet
from authadoptapp.models.pet import Pet
from authadoptapp.models.user import User
from rest_framework import serializers


class RequestPetSerializer(serializers.ModelSerializer):
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
        petID = validated_data.pop('pet')
        petData = Pet.objects.get(id=petID)

        userID = validated_data.pop('user')
        userData = User.objects.get(id=userID)

        requestPetInstance = RequestPet.objects.create(
            user=userData, pet=petData, **validated_data)

        return requestPetInstance

    def to_representation(self, obj):
        requestPet = RequestPet.objects.get(id=obj.id)
        user = User.objects.get(id=requestPet.user)
        pet = Pet.objects.get(id=requestPet.pet)
		
        return {
            'id': requestPet.id,
            'user': user,
            'pet': pet,
            'created_at': requestPet.created_at,
            'request_kind': requestPet.request_kind,
            'finalized_at': requestPet.finalized_at,
        }