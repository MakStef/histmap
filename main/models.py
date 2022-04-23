from django.db import models

# Create your models here.
class Level(models.Model):
    land_name = models.CharField(max_length=150, verbose_name = "Назва історичного об'єкту")
    since = models.IntegerField(verbose_name = "Рік створення")
    source = models.FileField(verbose_name = "Файл рівня")