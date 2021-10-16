from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authadoptapp.serializers.petSerializer import PetSerializer
from rest_framework.permissions import IsAuthenticated


class PetCreateView(views.APIView):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = serializer.save()

        return Response(serializer.to_representation(res), status=status.HTTP_201_CREATED)