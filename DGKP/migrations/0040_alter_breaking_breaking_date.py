# Generated by Django 4.2.7 on 2024-01-04 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0039_alter_breaking_breaking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 4, 11, 56, 17, 969251, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
