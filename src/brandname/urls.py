from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('Brandname', BrandnameViewSet, basename='brandname')

urlpatterns = [
    path('', include(router.urls)),
  
]