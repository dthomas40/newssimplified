from django.db import models
from django.utils import timezone
# Create your models here.

class PostManager(models.Manager):
    def create_post(self, title, content):
        post = self.create(title=title, content=content)
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
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    objects = PostManager()

    def __str__(self):
        return self.title