# Generated by Django 3.2.6 on 2021-08-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=70, verbose_name='Cidade'),
        ),
    ]