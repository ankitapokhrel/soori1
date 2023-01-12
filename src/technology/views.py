from django.shortcuts import render
from .serializers import TechnologySerializer
from .models import Technology
from rest_framework import viewsets

# Create your views here.
class TechnologyViewSet(viewsets.ModelViewSet):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializer
    