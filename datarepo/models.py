from django.db import models

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
    name=models.CharField(max_length=255)
    price=models.IntegerField()

