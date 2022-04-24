from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    auto_clickers = models.IntegerField()