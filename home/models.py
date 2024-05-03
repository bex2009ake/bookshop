from django.db import models
from auth_user.models import User
# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='aboutImg/')
    video = models.FileField(upload_to='aboutVideo/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    img = models.ImageField(upload_to='bookImg/')
    author = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    page_count = models.PositiveIntegerField()
    short_desc= models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    note = models.TextField()
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.client.phone