from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    size = models.CharField(max_length=20, verbose_name="Розмір")
    color = models.CharField(max_length=50, verbose_name="Колір")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return f"{self.brand} {self.name} ({self.size})"