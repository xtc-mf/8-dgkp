# Generated by Django 4.2.7 on 2024-01-07 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0053_material_material_quantity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breakingmaterial',
            options={'verbose_name': 'ЗаявкаМатериал', 'verbose_name_plural': 'ЗаявкиМатериалы'},
        ),
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 7, 11, 29, 45, 930073, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
