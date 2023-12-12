from django.db import models
from django.contrib.auth.models import User, auth
import datetime


# Create your models here.


class Categorie(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    # since url are of 2083 max characters
    image_url = models.ImageField(upload_to='Images/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products_by_categorieid(categorie_id):
        if categorie_id:
            return Product.objects.filter(category=categorie_id)
        else:
            return Product.objects.all()


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    address = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=13, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

