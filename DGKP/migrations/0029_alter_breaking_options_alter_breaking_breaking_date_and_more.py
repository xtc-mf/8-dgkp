# Generated by Django 4.2.7 on 2024-01-03 12:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DGKP', '0028_alter_breaking_breaking_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breaking',
            options={},
        ),
        migrations.AlterField(
            model_name='breaking',
            name='breaking_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 3, 12, 48, 33, 856798, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='BreakingMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, default=1.0, max_digits=5, verbose_name='Количество')),
                ('breaking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='DGKP.breaking')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DGKP.material')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
