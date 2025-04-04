from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import Clicker.models


class User(AbstractUser):
    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super(User, self).save(*args, **kwargs)
        if is_new:
            result = Clicker.models.Results(user=self)
            result.save()