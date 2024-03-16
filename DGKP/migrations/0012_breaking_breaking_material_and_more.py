# Generated by Django 4.2.7 on 2023-12-18 10:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0011_breaking_breaking_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='breaking',
            name='breaking_material',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='DGKP.material'),
        ),
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 18, 10, 26, 57, 548042, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
