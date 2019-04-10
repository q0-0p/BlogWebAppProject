from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField('date published')
