from rest_framework import serializers
from .models import Ourteam, MessagefromCEO

class OurteamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ourteam
        fields='__all__'

class MessagefromCEOSerializer(serializers.ModelSerializer):
    class Meta:
        model=MessagefromCEO
        fields='__all__'