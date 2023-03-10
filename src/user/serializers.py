from rest_framework import serializers
from src.user.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=['email', 'name', 'password', 'address', 'contact_info', 'password2']
        extra_kwargs={'password':{'write_only': True}}

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password!=password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")
            
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=100)
    class Meta:
        model=User
        fields=['email', 'password']