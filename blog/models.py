from django.db import models
from django.utils import timezone
# Create your models here.

class PostManager(models.Manager):
    def create_post(self, title, content):
        post = self.create(title=title, content=content)
        # do something with the book
        return post

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    objects = PostManager()

    def __str__(self):
        return self.title

post = Post.objects.create_post("Pride and Prejudice","Nothing to see here")
