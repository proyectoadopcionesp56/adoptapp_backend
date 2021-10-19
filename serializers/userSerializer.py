from rest_framework import serializers
from authadoptapp.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'lastname',
            'IDKind',
            'IDNumber',
            'address',
            'city',
            'country',
            'landline',
            'mobilephone',
            'jobs',
            'company',
            'username',
            'email',
            'password',
            'rol'
        ]

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'IDKind': user.IDKind,
            'IDNumber': user.IDNumber,
            'address': user.address,
            'city': user.city,
            'country': user.country,
            'landline': user.landline,
            'mobilephone': user.mobilephone,
            'jobs': user.jobs,
            'company': user.company,
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'rol': user.rol
        }