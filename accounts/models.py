from django.db import models
from django.db.models.signals import pre_save
import uuid
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
  
    id = models.CharField(primary_key=True, max_length=36, unique=True)  
    def __str__(self):
        return self.username
    
   
    
