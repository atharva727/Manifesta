from django.db import models  
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  
    email = models.EmailField(verbose_name="email", unique=True, max_length = 60)  
    username = models.CharField(max_length=50,unique=True)  
    is_vendor = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)  
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)  
    is_admin = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username'] 
  
    def __str__(self):
        return self.username
      