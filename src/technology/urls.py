from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('Technology', TechnologyViewSet, basename='technology')

urlpatterns = [
    path('', include(router.urls)),
  
]