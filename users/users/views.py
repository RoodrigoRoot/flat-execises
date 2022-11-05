from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import CreateProfileModelSerializer
from users.services import create_profile


class CreateProfileAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = CreateProfileModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = create_profile(serializer.data)
        if not response['success']:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_201_CREATED)