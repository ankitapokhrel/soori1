from rest_framework import serializers
from .models import Brandname

class BrandnameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brandname
        fields='__all__'
        