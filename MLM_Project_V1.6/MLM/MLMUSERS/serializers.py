from rest_framework import serializers
from MLMUSERS.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    #image = serializers.ImageField(max_length = None,use_url = True)
    image = serializers.ImageField(source='default.jpg', required=False)

    class Meta:
        model = Profile
        fields = ('number','first_name', 'last_name','AdharCard','Pancard','AltMobileNumber','image')