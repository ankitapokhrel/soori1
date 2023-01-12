from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.solution.views import *

router=DefaultRouter()
router.register('Solution', SolutionViewSet, basename='solution')

urlpatterns = [
    path('', include(router.urls)),
  
]