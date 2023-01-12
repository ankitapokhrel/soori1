from django.shortcuts import render
from .serializers import BrandnameSerializer
from .models import Brandname
from rest_framework import viewsets

# Create your views here.
class BrandnameViewSet(viewsets.ModelViewSet):
    queryset=Brandname.objects.all()
    serializer_class=BrandnameSerializer
    