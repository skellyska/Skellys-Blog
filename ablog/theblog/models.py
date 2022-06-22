from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    #defines what I want on the blog such as title, author, body
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        #allows admin to see blog title and author on admin page
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        #returns article detail view once post is created
        return reverse('home')

