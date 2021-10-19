from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authadoptapp.serializers.petSerializer import PetSerializer
from authadoptapp.models.pet import Pet
from django.http import Http404


class PetUpdateView(views.APIView):

    def get_object(self, pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
