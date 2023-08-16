# Generated by Django 4.2.4 on 2023-08-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=5)),
                ('buying', models.FloatField()),
                ('buyingstr', models.CharField(max_length=100)),
                ('selling', models.FloatField()),
                ('sellingstr', models.CharField(max_length=100)),
                ('rate', models.FloatField()),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('datetime', models.DateTimeField()),
                ('calculated', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Coin',
                'verbose_name_plural': 'Coins',
                'db_table': 'coins',
            },
        ),
    ]