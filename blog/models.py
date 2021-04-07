from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add = True) #date posted is current date and time when object is added/created
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) #what if user who creates the post is deleted? Delete their post

#dunder str method to print out the post title in CMD
    def __str__(self):
        return self.title
