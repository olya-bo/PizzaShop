from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адреса")
    logo = models.ImageField(upload_to='pizzashop_logo/', blank=False)

    def __str__(self):
        return self.name
