from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, address, contact_info, password=None, password2=None):
        # for creating user
        if not email:
            raise ValueError('Users must have an email address')

        user=self.model(
            email=self.normalize_email(email),
            name=name, 
            address=address,
            contact_info=contact_info,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, address, contact_info, password=None):
        user=self.create_user(
            email, 
            password=password,
            name=name,
            address=address,
            contact_info=contact_info,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(verbose_name='Email', max_length=255, unique=True)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    address=models.CharField(max_length=20)
    contact_info=PhoneNumberField(null=False, blank=False, unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name', 'address', 'contact_info']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):   
        # does the user have a specific permission?
        return self.is_admin

    def has_module_perms(self, app_label):   
        # does the user have permission to view the app 'app_label'?
        return True

    @property 
    def is_staff(self):  
        #is the user a member of staff?
        return self.is_admin