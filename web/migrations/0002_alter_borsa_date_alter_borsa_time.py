# Generated by Django 4.2.4 on 2023-08-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borsa',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='borsa',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]