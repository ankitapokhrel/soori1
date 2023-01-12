from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import viewsets

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    