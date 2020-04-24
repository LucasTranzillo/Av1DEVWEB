from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.DecimalField('price', decimal_places=2, max_digits=6)
    amount = models.IntegerField('amount')

class Client(models.Model):
    name = models.CharField('name', max_length=50)
    age= models.IntegerField('age')
    username = models.CharField('username', max_length=25)

class Service(models.Model):
    serviceType = models.CharField('servicetype', max_length=30)
    description = models.CharField('description', max_length=1000)
    price = models.DecimalField('price', decimal_places=2, max_digits=6)
