from django.urls import path, include
from src.user.views import UserlogInView, UserRegistrationView


urlpatterns = [ 
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserlogInView.as_view(), name='login'),

    
]