from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.petSerializer import PetSerializer


class PetCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = serializer.save()

        return Response(serializer.to_representation(res), status=status.HTTP_201_CREATED)
