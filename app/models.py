from django.db import models
from django.core.validators import MinLengthValidator


class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(validators=[MinLengthValidator(5)])
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text[:50])
