# Generated by Django 4.2.7 on 2024-03-01 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0082_alter_breaking_breaking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 1, 15, 50, 38, 971774, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
