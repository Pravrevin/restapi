from rest_framework import serializers
from . models import Share,Group

class CommentSerializer(serializers.Serializer):
    NumberOfShares = serializers.CharField(max_length=200)
    TotalAmount = serializers.CharField(max_length=200)
    UserId = serializers.CharField(max_length=200)


class GroupViewForUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ('share_id', 'group_id', 'user_id', 'created_date','s_status')


class GroupSerializer(serializers.Serializer):
    UserId = serializers.CharField(max_length=200)