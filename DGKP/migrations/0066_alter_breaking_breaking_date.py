# Generated by Django 4.2.7 on 2024-01-08 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0065_remove_material_material_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 8, 12, 34, 37, 513221, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
