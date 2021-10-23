from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authadoptapp.models.requestPet import RequestPet
from authadoptapp.serializers.requestPetSerializer import RequestPetSerializer


class RequestPetDetailsView(generics.ListAPIView):
    queryset = RequestPet.objects.all()
    serializer_class = RequestPetSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
