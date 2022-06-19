from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.title
    