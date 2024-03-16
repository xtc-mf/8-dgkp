# Generated by Django 4.2.7 on 2023-12-20 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0019_alter_breaking_breaking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 20, 9, 14, 18, 944983, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='breaking',
            name='breaking_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_volume',
            field=models.DecimalField(decimal_places=1, default=1.1, max_digits=3, verbose_name='Количество'),
        ),
    ]
