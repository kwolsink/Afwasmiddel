from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from authentication.models import AfwasmiddelUser


class RegistrationSerializer(ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        """
        Creates a new user
        :return: the user object
        """
        user = AfwasmiddelUser.objects.create_user(email=validated_data['email'], username=validated_data['username'],
                                                   password=validated_data['password'])
        return user

    class Meta:
        model = AfwasmiddelUser
        fields = ['email', 'username', 'password']
