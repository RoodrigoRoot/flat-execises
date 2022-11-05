from properties.serializers import PropertiesModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from properties.services import create_property



class CreatePropertiesAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PropertiesModelSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        response = create_property(serializer.data)
        if not response['success']:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_201_CREATED)


