# Generated by Django 4.0.3 on 2022-05-12 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Країна')),
                ('slug', models.SlugField(unique=True)),
                ('about', models.TextField(verbose_name='Опис країни')),
            ],
            options={
                'verbose_name': 'Країна',
                'verbose_name_plural': 'Країни',
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150, verbose_name='Текст посилання')),
                ('link', models.CharField(max_length=150, verbose_name='Посилання')),
            ],
            options={
                'verbose_name': 'Навігаційний елемент',
                'verbose_name_plural': 'Навігаційні елементи',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва поселення')),
                ('image', models.ImageField(upload_to='loc_images', verbose_name='Зображення поселення')),
                ('about', models.TextField(verbose_name='Опис місця')),
                ('slug', models.SlugField(unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.country')),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
            },
        ),
        migrations.CreateModel(
            name='History_Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name="Назва об'єкту")),
                ('about', models.TextField(verbose_name="Опис об'єкту")),
                ('layout', models.FileField(upload_to='layouts', verbose_name=".zip архів з макетом об'єкту")),
                ('slug', models.SlugField(unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.location')),
            ],
            options={
                'verbose_name': "Історичний об'єкт",
                'verbose_name_plural': "Історичні об'єкти",
            },
        ),
    ]
