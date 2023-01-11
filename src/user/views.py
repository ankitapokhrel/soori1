from django.shortcuts import render
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  #for jwt authentication
from .renderers import UserRenderer

# to get token using simple jwt auth.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_class=[UserRenderer]
    def post(self, request, format=None):
        serializer= UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            return Response({'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserlogInView(APIView):
    
    def post(self, request, format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email, password=password)
            if user is not None: 
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'non_field_errors':['Email or Password is not valid']}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

