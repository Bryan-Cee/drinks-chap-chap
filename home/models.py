from django.db import models


class Drinks(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    src = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

