from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manager for User Profile '''
    def create_user(self, email, name, password=None):
        '''Will create a User Profile '''
        if not email:
            raise ValueError("Users must have an Email id")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name,)

        user.set_password(password)    #set_password will encrypt the password by default
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Database model for users in system '''
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    #password and email are by default required
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fulllname(self):
        return self.name

    def get_shortname(self):
        return self.name

    def __str__(self):
        return self.email
