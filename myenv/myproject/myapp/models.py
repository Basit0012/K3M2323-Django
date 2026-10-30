from django.db import models

# Create your models here.
class Emp(models.Model):
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250)
    salary = models.IntegerField()
    age = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()