# Generated by Django 4.2.7 on 2024-01-08 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0063_alter_breaking_breaking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 8, 11, 20, 9, 510620, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
