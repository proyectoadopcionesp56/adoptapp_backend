from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authadoptapp.serializers.requestPetSerializer import RequestPetSerializer
from rest_framework.permissions import IsAuthenticated


class RequestPetCreateView(views.APIView):
    serializer_class = RequestPetSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = RequestPetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = serializer.save()

        return Response(serializer.to_representation(res), status=status.HTTP_201_CREATED)
