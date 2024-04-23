from django.db import models
from django.shortcuts import reverse , render , redirect
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name}'
    
    @classmethod
    def get_all_category(cls):
        return cls.objects.all()
    
    @classmethod
    def get_specific_category(cls, id):
        return cls.objects.get(id=id)



class Library(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='library/images/', null=True, blank=True)
    no_of_item = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name
    


    @classmethod
    def get_all_products(cls):
        return  cls.objects.all()
    
    @classmethod
    def get_specific_products(cls, id):
        return  cls.objects.get(id=id)
    

    def get_image_url(self):
        return f'/media/{self.image}'
    
    def get_show_url(self):
        return reverse('library.show',args=[self.id])

    def get_edit_url(self):
        return reverse('library.edit',args=[self.id])
    

    def get_edit_urlcategory(self):
        return reverse('library.editcategory',args=[self.id])

class BorrowingModel(models.Model):
    user_name = models.CharField(max_length=255)  
    book_name = models.CharField(max_length=255)  
    borrowed_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.deadline:
            self.deadline = self.borrowed_date + timedelta(days=7)
        super(BorrowingModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user_name} borrowed {self.book_name} on {self.borrowed_date}'