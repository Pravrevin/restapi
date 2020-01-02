from rest_framework import serializers
from MLMAPP.models import RegistrationDetails

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationDetails
        fields = ('username', 'email', 'password','mobilenumber','refercode')

        def create(self, validated_data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return RegistrationDetails.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Snippet` instance, given the validated data.
            """
            instance.title = validated_data.get('title', instance.title)
            instance.code = validated_data.get('code', instance.code)
            instance.save()
            return instance
