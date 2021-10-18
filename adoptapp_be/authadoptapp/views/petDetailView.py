from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from authadoptapp.models.pet import Pet
from authadoptapp.serializers.petSerializer import PetSerializer


class PetDetailView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
