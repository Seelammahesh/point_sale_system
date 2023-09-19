import datetime

from django.db import models
from django.db.models.fields import DateField,TimeField
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)


    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    name= models.CharField(max_length=255)

    def __str__(self):
        return str(self.category)


class Product(models.Model):
    sub_category=models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(blank=True,null=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

