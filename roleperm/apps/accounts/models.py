from django.db import models

# Create your models here.


class Customers(models.Model):
    name = models.CharField(max_length=200,null=True)
    place = models.CharField(max_length=200)
    email = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    CATEGORY = (
        ('Out Door','out door'),
        ('Indoor','indoor'),
    )
    name = models.CharField(max_length=200,null=True)
    price= models.FloatField(null=True)
    description = models.TextField(null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    category = models.CharField(max_length=20,choices=CATEGORY)

    def __str__(self):
        return self.name
    

class Orders(models.Model):
    customer = models.ForeignKey(Customers,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    STATUS = (
        ('Pending','pending'),
        ('Out of Delivary','out of delivary'),
        ('Delivered','Delivered')
    )
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=20,choices=STATUS)
    