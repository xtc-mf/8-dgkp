# Generated by Django 4.2.7 on 2024-03-10 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0093_alter_breaking_breaking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 10, 20, 23, 33, 939237, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
