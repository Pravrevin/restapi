from rest_framework import serializers
from MLMUSERS.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_lenth = None,use_url = True)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','AdharCard','Pancard','AltMobileNumber','image')