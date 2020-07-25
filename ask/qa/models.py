from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_new_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForiegnKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
