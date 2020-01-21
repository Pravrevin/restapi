from rest_framework import serializers



class TicketSerializer(serializers.Serializer):
    Issue = serializers.CharField(max_length=200)
    Description = serializers.CharField(max_length=200)