# Generated by Django 4.2.7 on 2024-01-07 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0054_alter_breakingmaterial_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 7, 11, 31, 40, 922311, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='breakingmaterial',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=1, default=1.0, max_digits=5, verbose_name='Количество'),
        ),
    ]
