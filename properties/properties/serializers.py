from rest_framework import serializers

from properties.models import Property


class UserSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=255)



class PropertiesModelSerializer(serializers.ModelSerializer):

    owner = serializers.JSONField()

    class Meta:
        model = Property
        fields = ("owner", "asking_price", "m2", "property_type", "city", "state", "street_name", "ext_number", "int_number", "neighborhood", "zip_code")


