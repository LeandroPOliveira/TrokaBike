# Generated by Django 4.2.3 on 2024-01-19 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0006_alter_bikes_data_fotografia_alter_bikes_descricao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikes',
            options={'verbose_name_plural': 'produtos'},
        ),
        migrations.AlterField(
            model_name='bikes',
            name='categoria',
            field=models.CharField(choices=[('MOUNTAIN', 'Mountain'), ('ROAD', 'Road'), ('GRAVEL', 'Gravel'), ('VESTUARIO', 'Vestuario')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
