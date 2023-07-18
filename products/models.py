from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1200)
    price = models.FloatField()
    image = models.ImageField(upload_to='products')
    menu = models.ForeignKey('Menu',on_delete=models.CASCADE,related_name='product_menu')
    def __str__(self):
        return self.name


    



class Menu(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    