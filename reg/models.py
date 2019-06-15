from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_date = models.DateTimeField(auto_created=True, auto_now=True)
    main_photo = models.ImageField(upload_to='images', height_field=None, width_field=None,
                                   max_length=100, null=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    comm = models.TextField()
    create_date = models.DateTimeField(auto_created=True, auto_now=True)
