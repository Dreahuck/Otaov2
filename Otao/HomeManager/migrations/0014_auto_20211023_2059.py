# Generated by Django 3.0.8 on 2021-10-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeManager', '0013_auto_20211023_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='id',
        ),
        migrations.AlterField(
            model_name='crypto',
            name='code',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='quantite',
            field=models.DecimalField(decimal_places=9, default=0, max_digits=10),
        ),
    ]
