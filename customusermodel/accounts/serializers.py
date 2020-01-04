from rest_framework import serializers
from accounts.models import MyUser

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'number','password')