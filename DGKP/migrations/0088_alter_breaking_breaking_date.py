# Generated by Django 4.2.7 on 2024-03-05 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0087_alter_breaking_breaking_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 5, 17, 57, 53, 647045, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
