# Generated by Django 4.2.3 on 2023-08-02 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_bikes_categoria_alter_bikes_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bikes',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
