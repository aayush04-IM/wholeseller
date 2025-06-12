from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.brand})"

class Sales(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs in {self.city.name}"
