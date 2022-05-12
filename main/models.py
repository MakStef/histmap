from django.db import models
from histmap.settings import MEDIA_URL

# Models here
class Country(models.Model):

    name=models.CharField(verbose_name="Країна", max_length=150)
    slug = models.SlugField(unique=True)
    about = models.TextField(verbose_name="Опис країни")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name="Країна"
        verbose_name_plural = "Країни"
class Location(models.Model):
    name = models.CharField(verbose_name="Назва поселення", max_length=150)
    image = models.ImageField(verbose_name="Зображення поселення", upload_to="loc_images")
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    about = models.TextField(verbose_name="Опис місця")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name="Місто"
        verbose_name_plural = "Міста"
class History_Object(models.Model):
    name = models.CharField(verbose_name="Назва об'єкту", max_length=150)
    about = models.TextField(verbose_name="Опис об'єкту")
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    layout = models.FileField(verbose_name=".zip архів з макетом об'єкту", upload_to="layouts")
    slug = models.SlugField(unique=True)

    def __str__(self):
            return f"{self.name} | {self.location.name}"
    class Meta:
        verbose_name="Історичний об'єкт"
        verbose_name_plural = "Історичні об'єкти"
class Navigation(models.Model):
    text = models.CharField(verbose_name="Текст посилання", max_length=150)
    link = models.CharField(verbose_name="Посилання", max_length=150)

    def __str__(self):
        return f"{self.link}"
    class Meta:
        verbose_name="Навігаційний елемент"
        verbose_name_plural = "Навігаційні елементи"