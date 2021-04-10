from django.db import models

# Create your models here.

class Article(models.Model):
    topic = models.CharField(max_length=30)
    field_name = models.TextField()