import asyncio
from properties.serializers import PropertiesModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from properties.services import create_property
from propertiesMS.broker import KafkaBroker



class CreatePropertiesAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PropertiesModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = create_property(serializer.data)
        response_kafka = serializer.data
        response_kafka.pop('owner')
        print(response_kafka)
        asyncio.run(
                KafkaBroker().send_message(response_kafka)
            )
        if not response['success']:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_201_CREATED)


