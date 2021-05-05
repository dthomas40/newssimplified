from django.db import models
from django.utils import timezone
# Create your models here.

class PostManager(models.Manager):
    def create_post(self, title, content, genre, author1, author2, url1, url2):
        post = self.create(title=title, content=content, genre=genre, author1=author1, author2=author2, url1=url1, url2=url2)
        # do something with the book
        return post

class Post(models.Model):

    GENRE_CHOICES = [
        ('W', 'World'),
        ('F', 'Finance'),
        ('P', 'Politics'),
        ('S', 'Science & Technology'),
        ('H', 'Health'),
        ('E', 'Entertainment')
    ]

    title = models.CharField(max_length=100)
    author1 = models.CharField(max_length=100)
    author2 = models.CharField(max_length=100)
    url1 = models.CharField(max_length=400)
    url2 = models.CharField(max_length=400)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, default='W')
    objects = PostManager()

    def __str__(self):
        return self.title