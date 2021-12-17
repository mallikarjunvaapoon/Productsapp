from django.db import models
from user.models import UserModel


class Comment(models.Model):
    comment_box = models.TextField(max_length=255)

    def __str__(self):
        return self.comment_box


class Feed(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_by = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)