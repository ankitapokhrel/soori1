from django.shortcuts import render
from .serializers import SolutionSerializer
from .models import Solution
from rest_framework import viewsets

# Create your views here.
class SolutionViewSet(viewsets.ModelViewSet):
    queryset=Solution.objects.all()
    serializer_class=SolutionSerializer
    