from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_new_add = True)
    rating = models.IntegerField(default = 0)
    author = models.ForiegnKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'question_like_user')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_new_add = True)
    question = models.ForiegnKey(Question, on_delete = models.CASCADE)
    author = models.ForiegnKey(User, on_delete = models.CASCADE)

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')