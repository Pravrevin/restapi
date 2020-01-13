from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    NumberOfShares = serializers.CharField(max_length=200)
    TotalAmount = serializers.CharField(max_length=200)
    UserId = serializers.CharField(max_length=200)


class GroupSerializer(serializers.Serializer):
    UserId = serializers.CharField(max_length=200)


class ShareSerializer(serializers.Serializer):
    UserId = serializers.CharField(max_length=200)
    GroupId = serializers.CharField(max_length=200)