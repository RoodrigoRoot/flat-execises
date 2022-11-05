from rest_framework import serializers

from django.contrib.auth.models import User

from users.models import Profile

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CreateProfileModelSerializer(serializers.ModelSerializer):

    user = CreateUserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'phone')

