from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(verbose_name="Назва міста", max_length=30)
    image = models.ImageField(verbose_name="Зображення міста")

    def __str__(self):
        return f"{self.name}"

class Navigation(models.Model):
    text = models.CharField(verbose_name="Текст посилання", max_length=150)
    link = models.CharField(verbose_name="Посилання", max_length=150)

    def __str__(self):
        return f"{self.link}"