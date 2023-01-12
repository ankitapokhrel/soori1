from django.shortcuts import render
from .models import MessagefromCEO, Ourteam
from .serializers import OurteamSerializer, MessagefromCEOSerializer
from rest_framework import viewsets

# Create your views here.
class OurteamViewSet(viewsets.ModelViewSet):
    queryset=Ourteam.objects.all()
    serializer_class=OurteamSerializer

class MessagefromCEOViewSet(viewsets.ModelViewSet):
    queryset=MessagefromCEO.objects.all()
    serializer_class=MessagefromCEOSerializer
    