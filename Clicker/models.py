from django.db import models

import users.models


class Tentacles(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default='Tentacle')
    cost = models.IntegerField(default=0)
    power = models.IntegerField(default=1)
    image = models.ImageField(upload_to='tentacles_images', null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = verbose_name = 'Тентакли'

    def __str__(self):
        return f'{self.name}'


class Results(models.Model):
    user = models.ForeignKey(to=users.models.User, on_delete=models.CASCADE)
    tentacle = models.ForeignKey(Tentacles, on_delete=models.CASCADE)
    tentacle_quantity = models.PositiveIntegerField(default=0)
    score = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'Результаты {self.user.username}'

    def click(self):
        self.score += self.click_power
        return self

    def check_level(self):
        check_points = [50000, 250000, 6250000]
        for i in range(1, 4):
            if self.score >= check_points[i-1] and self.level < i:
                self.level = i