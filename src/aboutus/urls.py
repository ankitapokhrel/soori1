
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('Ourteam', OurteamViewSet, basename='ourteam')
router.register('MessagefromCEO', MessagefromCEOViewSet, basename='messagefromCEO')

urlpatterns = [
    
    path('', include(router.urls)),
]
