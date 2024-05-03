from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not bool(phone) or not bool(password):
            raise ValueError('Phone number or email are wrong !!!')
        
        if not len(password) >= 8:
            raise ValueError('Password len must be minimum 8 chars')
        
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone=phone, password=password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = ['password']

    objects = UserManager()


    def __str__(self) -> str:
        return self.phone
    

class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    lastt_name = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to='user/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.user.phone