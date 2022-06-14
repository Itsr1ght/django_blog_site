from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    date = models.DateField()
    image = models.ImageField()
