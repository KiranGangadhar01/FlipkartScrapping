from django.db import models

class Information(models.Model):
    productName = models.CharField(max_length=128, unique=True)
    productPrice = models.IntegerField(default=1)
    minPrice = models.IntegerField(default=1)
    maxP = models.IntegerField(default=1)
