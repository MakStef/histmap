# Generated by Django 4.0.3 on 2022-04-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=26, verbose_name='Назва міста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('about', models.TextField(verbose_name='Про місто')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Фото-аватар міста')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Назва місця')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('source', models.FileField(upload_to='', verbose_name='Файл рівня')),
            ],
        ),
    ]
