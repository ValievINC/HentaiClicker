from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self):
        self.score += self.click_power
        return self
