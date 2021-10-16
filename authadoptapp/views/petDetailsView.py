from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authadoptapp.models.pet import Pet
from authadoptapp.serializers.petSerializer import PetSerializer


class PetDetailsView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
