# Generated by Django 4.2.7 on 2024-01-02 12:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0026_alter_breaking_breaking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='breaking',
            name='breaking_worker_fullname',
            field=models.CharField(default='NaN', max_length=200, verbose_name='ФИО выполняющего'),
        ),
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 2, 12, 40, 5, 981445, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='breaking',
            name='breaking_material',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='DGKP.material', verbose_name='Материал'),
        ),
    ]
