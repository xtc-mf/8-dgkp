# Generated by Django 4.2.7 on 2023-12-27 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0025_alter_breaking_breaking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 27, 20, 38, 48, 105425, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
