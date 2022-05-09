from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=125, default='N K')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Grocery(models.Model):
    product_tag = models.CharField(max_length=15)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, related_name='grocery', on_delete=models.CASCADE, default='grocery')
    price = models.FloatField()
    quantity = models.IntegerField()
    imageurl = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name
