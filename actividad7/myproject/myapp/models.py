from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
