from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=0)

    # Тентакли
    tentacle1_count = models.IntegerField(default=0)
    tentacle2_count = models.IntegerField(default=0)
    tentacle3_count = models.IntegerField(default=0)
    tentacle4_count = models.IntegerField(default=0)
    tentacle5_count = models.IntegerField(default=0)

    # Стоимость Тентаклей
    tentacle1_cost = models.IntegerField(default=10)
    tentacle2_cost = models.IntegerField(default=100)
    tentacle3_cost = models.IntegerField(default=1000)
    tentacle4_cost = models.IntegerField(default=10000)
    tentacle5_cost = models.IntegerField(default=100000)

    # Собственно логика клика
    def click(self):
        self.score += self.click_power
        return self

    # Выдача уровня в зависимости от того, какого счёта добился игрок
    def check_level(self):
        check_points = [50000, 250000, 6250000]
        for i in range(1, 4):
            if self.score >= check_points[i-1] and self.level < i:
                self.level = i
