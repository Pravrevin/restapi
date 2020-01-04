from rest_framework import serializers
from MLMAPP.models import MyUser

class RegistrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = MyUser.objects.create(
            username=validated_data['username'],
            email = validated_data['email'],
            number = validated_data['number'],
            refercode = validated_data['refercode']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'number','refercode','password')
        extra_kwargs = {
            'password' : {'write_only':True}
        }
