from django.db import models

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=1000)
    article_subtitle = models.CharField(max_length=1000)
    article_description = models.TextField(max_length=10000)
    picture_1 = models.ImageField()
    picture_2 = models.ImageField()
    picture_3 = models.ImageField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.article_title + " ---->>> " + self.author

class Team(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    picture = models.ImageField()
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name
