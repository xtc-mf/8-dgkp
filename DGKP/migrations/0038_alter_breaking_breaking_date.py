# Generated by Django 4.2.7 on 2024-01-04 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0037_alter_breaking_breaking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 4, 11, 54, 26, 511436, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
