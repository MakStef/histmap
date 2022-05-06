from django.db import models


# Models here
class Country(models.Model):
    class Meta:
                verbose_name_plural = u'Countries'

    name=models.CharField(verbose_name="Країна", max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"
class Location(models.Model):
    name = models.CharField(verbose_name="Назва поселення", max_length=150)
    image = models.ImageField(verbose_name="Зображення поселення")
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"
class History_Object(models.Model):
    name = models.CharField(verbose_name="Назва об'єкту", max_length=150)
    about = models.TextField(verbose_name="Опис об'єкту")
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    slug = models.SlugField()
class Navigation(models.Model):
    text = models.CharField(verbose_name="Текст посилання", max_length=150)
    link = models.CharField(verbose_name="Посилання", max_length=150)

    def __str__(self):
        return f"{self.link}"