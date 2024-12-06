from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    categories = models.ManyToManyField(Category, related_name='posts')  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

    # list_idisplay  für filtering -> Recherche

    def __str__(self):
        return self.title
