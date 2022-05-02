# Generated by Django 2.1.2 on 2022-04-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenicspots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spots',
            name='x',
            field=models.DecimalField(decimal_places=6, default=120.7, max_digits=9, verbose_name='经度'),
        ),
        migrations.AlterField(
            model_name='spots',
            name='y',
            field=models.DecimalField(decimal_places=6, default=28.0, max_digits=9, verbose_name='纬度'),
        ),
    ]
